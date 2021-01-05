"""
All dynamic routing belongs here 
"""

import os, json, ast, random, requests
from flask import render_template, redirect, flash, url_for, request, jsonify, Request, send_file, make_response, session, abort, Response, get_template_attribute
from flask_login import current_user, login_user, logout_user, login_required
from controllers import app, bcrypt, mail, oauth
from datetime import timedelta
from controllers.forms import RegistrationForm, LoginForm, Billing, PaymentInfo, ContactUsForm, PasswordForm, Disable, Activate, ChangePasswordForm
from controllers.forms import RegistrationForm, LoginForm, AdminAddProductForm, AdminUpdateProductForm, UpdateAccountForm, UpdateBilling, RequestResetForm, ResetPasswordForm, UpdateCard
from controllers.Sentemail import sendEmail, adminEmail
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_mail import Message
from flask import Flask
from controllers import key
import base64, platform
from password_strength import PasswordPolicy
from password_strength import PasswordStats
from datetime import datetime, timedelta
from flask_csv import send_csv
import threading
from time import sleep 
import logging
from controllers.qr import send_qr_code
import random
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import pyodbc
from flask import current_app
from flask_bcrypt import generate_password_hash, check_password_hash


# Database #
server = 'ispj-database.database.windows.net'
database = 'ISPJ Database'
username = 'Peter'
password = 'p@ssw0rd'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn.cursor()

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
###Create Log file ###

def setup_logger(name, log_file, level):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
    

errors = setup_logger('Error_logger', 'errors.log', logging.ERROR)
infos = setup_logger('Info_logger', 'infos.log', logging.INFO)
criticals = setup_logger('Criticals_logger', 'criticals.log', logging.CRITICAL)
debugs = setup_logger('debugs_logger', 'debugs.log', logging.DEBUG)

"""
Functions/Utilities 
"""
# Refreshes Admin events #
def refreshEvents():
    with open('json_files/events.json', 'r+') as f:
        data = json.load(f)
    return data

# Refreshes Admin Analytics #
def refreshAnalytics():
    with open('json_files/analytics.json', 'r+') as f:
        data = json.load(f)
    return data 

# Verify reset token #
def verify_reset_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token)['user_id']
    except:
        return None
    return query('SELECT * FROM user_accounts WHERE id=?', user_id)[0]

# Constructs an sql query with any number of parameters passed in for query to be constructued #
"""
For insert, delete, update statements 
"""
def constructAndExecuteQuery(query, *args):
    cursor.execute(query, *args)
    conn.commit()

"""
For select statements
"""
def query(query, *args):
    try:
        cursor.execute(query, *args)
        result = cursor.fetchall()
    except: 
        result = []
    return result

# Ensures that allowed images are accepted #
def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    print(filename)
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False
# @app.context_processor
# def inject_dict_for_all_templates():
#     allProducts = query('SELECT * FROM products')
#     test = query("select prod_name from products")
#     game_list = []
#     for row in test:
#         game_list.append(row[0])
#     return dict(game_list=game_list,allProducts=allProducts)
# Sends a qr code to the user upon payment and starts an internal thread #
@app.route('/qr')
def qr():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
        email = query('SELECT email FROM user_accounts WHERE Id=?', session['user_id'])[0][0]
        fullname = query('SELECT fullname FROM user_accounts WHERE Id=?', session['user_id'])[0][0]
        global otp
        otp = send_qr_code(email, fullname)
        threading.Thread(target=tasks).start()
        return str(otp)
    else: 
        return redirect(url_for('home'))

# Threading #
lock_timer = 0
def task():
    global lock_timer 
    lock_timer = 300
    for i in range(300):
        lock_timer -= 1
        sleep(1)
        print(lock_timer)
    print('finished')

# Send an email to the admin email #
def emailTask():
    global email
    with app.app_context():
        adminEmail(email)
    return "sent"

# Timer ajax route #
@app.route('/timer')
def timerr():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest': 
        global timer
        return str(timer)
    else:
        return redirect(url_for('home'))

# Lockout ajax route #
@app.route('/lock_timer')
def lock_timerr():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest': 
        global lock_timer
        print(lock_timer)
        return str(lock_timer)
    else:
        return redirect(url_for('home'))

# set session lifetime to 15 minutes #
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)

# Check Password ajax route #
@app.route('/checkPassword')
def checkpassword():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
        datas = {"data":[]}
        password = request.args.get('pass')
        policy = PasswordPolicy.from_names(
            length = 8,
            uppercase = 2,
            numbers = 2,
            special = 2, 
            nonletters = 2
        )
        stats = PasswordStats(password)
        requirements = policy.test(password)
        for i in range(len(requirements)):
            requirements[i] = str(requirements[i])
        return json.dumps({"data":[stats.strength(), f"{requirements}"]})
    else:
        return redirect(url_for('home'))

"""
Home, contact-us, about pages, Chatbot
"""

# Chatbot starting Output #
output = [("message stark", {"text":"Hi, how may I assist you?"})]

# Home Page #
@app.route('/')
def home():
    test = query("select prod_name from products")
    game_list = []
    for row in test:
        game_list.append(row[0])
    print(game_list)
    return render_template('homepage.html',game_list=game_list)

# FAQ Page #
@app.route('/faq')
def faq():
    test = query("select prod_name from products")
    game_list = []
    for row in test:
        game_list.append(row[0])
    return render_template('faq.html', result=output,game_list=game_list)

# Chatbot #
@app.route('/result',methods=["POST","GET"])
def Result():
    global output
    if request.method=="POST":
        result=list(request.form.values())[0]
        if request.args.get('game') != None:
            result = request.args.get('game')
        if result.lower()=="restart":
            output = [("message stark", {"text":"Hi, how may I assist you?"})]
        elif result == '':
            output.extend([("message parker",{"text":result})])
            output.extend([("message stark", {"text":"Sorry I didn't get that..."})])
        else:
            try:
                r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": result})
                li = []
                for i in r.json():
                    if 'image' in i:
                        li.append({"pic": i['image']})
                    if 'text' in i:
                        li.append(i['text'])
                    if 'buttons' in i:
                        for x in i['buttons']:
                            li.append((x['title'], "button"))
                sample = [("message parker",{"text":result})] 
                buttons = []
                for count, msg in enumerate(li): 
                    if count != len(li)-1 and type(li[count+1]) is dict:
                        sample.append(("message stark", {"text":msg, "pic": li[count+1]["pic"]}))
                    elif type(li[count]) is tuple:
                        buttons.append(msg[0])
                    elif type(li[count]) is not dict:
                        sample.append(("message stark", {"text":msg}))
                if buttons != []:
                    sample.append(("message stark", {"button":buttons}))
                output.extend(sample)
            except:
                output.extend([("message parker", result), ("message stark", "We are unable to process your request at the moment. Please try again...")])
        return render_template("faq.html",result=output)

# About page #
@app.route('/about')
def about():
    return render_template('aboutus.html')

# Contact Us page #
@app.route('/contactUs', methods=['GET', 'POST'])
def contactUs():
    form = ContactUsForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.fullname.data
        email = form.email.data
        comment = form.message.data
        case_id = query('SELECT case_id FROM contact_us_records')
        if case_id == []:
            req = 'INSERT INTO contact_us_records VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);'
            constructAndExecuteQuery(req, 1, name, email, comment, 0, 0, 0, 0, 0)
        else:
            lastCase = case_id[-1][0]
            req = 'INSERT INTO contact_us_records VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);'
            constructAndExecuteQuery(req, int(lastCase)+1, name, email, comment, 0, 0, 0, 0, 0)
        return redirect(url_for("home"))
    return render_template("contactUs.html", form=form)

"""
Account Related Routes 
"""

# Register Account route # 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if "user_id" in session:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.fullname.data
        password = form.password.data
        hash_pasword = generate_password_hash(password, 10)
        email = form.email.data.strip()
        if query('SELECT * FROM user_accounts WHERE email=?', email) != []:
            flash('This email has been taken already!', 'danger')
            return redirect(url_for('login'))
        previousPass = []
        previousPass.append(hash_pasword)
        constructAndExecuteQuery('INSERT INTO user_accounts VALUES(?, ?, ?, ?, ?, ?, ?, ?)', random.randint(100000, 999999), 1, email, hash_pasword, 0, '../static/img/profile_pic/default.jpg', str(previousPass), name)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# Login Route #
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    global email
    if lock_timer != 0:
        form = LoginForm()
        flash('Please re-attempt login in 5 mins','danger')
        return render_template('login.html', title='Login', form=form, locked="true")
    if "attempts" not in session:
        session['attempts'] = 5
    if form.validate_on_submit():
        email = form.email.data.strip()
        user = query('SELECT * FROM user_accounts WHERE email = ?', email)
        if user == []: 
            flash('Please check your credentials again', 'danger')
            return render_template('login.html', form=form)
        user_password = user[0][3]
        # hashing of password
        password = form.password.data
        hash_successful = check_password_hash(user_password, password)
        if user and hash_successful == True:
            user_id = user[0][0]
            user_active = user[0][1]
            user_email = user[0][2]
            if user_active == False:
                return redirect(url_for('activateask'))
            session['user_id'] = user_id
            infos.info('%s logged in successfully', user_email)
            session['attempts'] = 5
            return redirect(url_for('home'))
        else:
            user_id = user[0][0]
            user_active = user[0][1]
            user_email = user[0][2]
            infos.info('%s failed to log in', user_email)
            attempt= session.get('attempts')
            attempt -= 1
            session['attempts']=attempt
            if attempt==1:
                flash('This is your last attempt, you will be blocked for 5mins, Attempt %d of 5'  % (attempt), 'danger')
            elif attempt == 0:
                threading.Thread(target=task).start()
                threading.Thread(target=emailTask).start()
                session['attempts'] = 5
                return redirect(url_for('login'))
            else:
                flash('Invalid login credentials, Attempts %d of 5'  % attempt, 'danger')
        return render_template('login.html', form=form)
    else:
        if "user_id" in session:
            return redirect(url_for('home'))
        form = LoginForm()
        return render_template('login.html', title='Login', form=form)

@app.route("/googlelogin")
def googlelogin():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route("/login/callback")
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    user = oauth.google.userinfo()
    session['profile'] = user_info
    session.permanent = True
    user = query('SELECT * FROM user_accounts WHERE Id = ?', session['profile']['id'])
    if not user:
        constructAndExecuteQuery("""Insert into user_accounts(Id,email,profile_image,fullname,account_status,isadmin) values (?,?,?,?,1,0)""",session['profile']['id'],session['profile']['email'],session['profile']['picture'],session['profile']['given_name'])
        user = query('SELECT * FROM user_accounts WHERE Id = ?', session['profile']['id'])
        session['user_id'] = user[0][0]
        return redirect('/myAccount')
    if user:
        session['user_id'] = user[0][0]
    return redirect('/myAccount')

# Adding Address route #
@app.route('/addAddress', methods=['GET', 'POST'])
def addAddress():
    form = Billing()
    if form.validate_on_submit():
        new_address = form.address.data 
        new_country = form.country.data 
        new_state = form.state.data 
        new_postal = form.postal.data
        all_address_list = query('SELECT * FROM Addresses')
        if all_address_list == []:
            all_address_list = [(0,)]
        strip_address = new_address.strip()
        existing_address = query('SELECT * FROM Addresses WHERE user_id=? AND address=?', session['user_id'], strip_address)
        if existing_address == []:
            user_exisiting_addresses = query('SELECT * FROM Addresses WHERE user_id=?', session['user_id'])
            if user_exisiting_addresses != []:
                for i in user_exisiting_addresses:
                    constructAndExecuteQuery('UPDATE Addresses SET default_address=? WHERE Id=?',"False",i[0])
            constructAndExecuteQuery('INSERT INTO Addresses VALUES(?,?,?,?,?,?,?)',int(all_address_list[-1][0])+1,new_address,new_state,new_country,new_postal,"True",session['user_id'])
            return redirect(url_for('myAccount'))
        else:
            flash('Address already added! Please add a different address', 'danger')
            return render_template('addAddress.html', form=form)
    else:
        return render_template('addAddress.html', form=form)

# Edit Address route #
@app.route('/editAddress', methods=['GET', 'POST'])
def editAddress():
    form=Billing()
    if request.method == 'GET':
        address_id = request.args.get('address')
        if address_id != None:
            address = query('SELECT * FROM Addresses WHERE Id=?', int(address_id))
            if address[0][-1] != int(session['user_id']):
                address = []
        else:
            return redirect(url_for('home'))
        return render_template('editAddress.html', form=form, address=address[0])
    if form.validate_on_submit():
        address_id = request.args.get('address')
        address = query('SELECT * FROM Addresses WHERE Id=?', int(address_id))
        editted_address = form.address.data 
        editted_country = form.country.data 
        editted_state = form.state.data 
        editted_postal = form.postal.data
        stripped_address = editted_address.strip()
        old_addresses = query('SELECT * FROM Addresses WHERE user_id=?', int(session['user_id']))
        if len(old_addresses) == 1:
            constructAndExecuteQuery('UPDATE Addresses SET address=?,state=?,Country=?,PostalCode=? WHERE Id=?',stripped_address, editted_state, editted_country, editted_postal, int(address_id))
            return redirect(url_for('myAccount'))
        else:
            check_existing_address = query('SELECT * FROM Addresses WHERE address=? AND user_id=?', stripped_address, int(session['user_id']))
            if check_existing_address == []:
                constructAndExecuteQuery('UPDATE Addresses SET address=?,state=?,Country=?,PostalCode=? WHERE Id=?',stripped_address, editted_state, editted_country, editted_postal, int(address_id))
                return redirect(url_for('myAccount'))
            elif check_existing_address[0][0] == int(address_id):
                constructAndExecuteQuery('UPDATE Addresses SET address=?,state=?,Country=?,PostalCode=? WHERE Id=?',stripped_address, editted_state, editted_country, editted_postal, int(address_id))
                return redirect(url_for('myAccount'))
            else:
                flash('You have already added this address! Please add a different address', 'danger')
                return render_template('editAddress.html', form=form,address=address[0])
    else:
        address_id = request.args.get('address')
        if address_id != None:
            address = query('SELECT * FROM Addresses WHERE Id=?', int(address_id))
        else:
            return redirect(url_for('home'))
        return render_template('editAddress.html', form=form, address=address[0])

# Setting Default Address route #
@app.route('/defaultAddress', methods=['GET', 'POST'])
def defaultAddress():
    address = request.args.get('address')
    if address == None:
        return redirect(url_for('home'))
    try:
        addressList = query('SELECT * FROM Addresses WHERE user_id=?', session['user_id'])
        test = address.strip()
        for i in addressList:
            constructAndExecuteQuery('UPDATE Addresses SET default_address=? WHERE Id=?',"False",int(i[0]))
        constructAndExecuteQuery('UPDATE Addresses SET default_address=? WHERE Id=?',"True",int(address))
        return "[]"
    except:
        return redirect(url_for('home'))

# Remove address route #
@app.route('/removeAddress')
def removeAddress():
    address = request.args.get('address')
    if address == None: 
        return redirect(url_for('myAccount'))
    try:
        test = address.strip()
        constructAndExecuteQuery('DELETE FROM Addresses WHERE Id=?', int(test))
        addresslist = query('SELECT * FROM Addresses WHERE user_id=?',session['user_id'])
        if addresslist != []:
            constructAndExecuteQuery('UPDATE Addresses SET "default_address"=? WHERE Id=?',"True",addresslist[-1][0])
        return "[]"
    except:
        return redirect(url_for('myAccount'))

# Add Card route #
@app.route('/addCard', methods=['GET','POST'])
def addCard():
    form = PaymentInfo()
    if form.validate_on_submit():
        card_name = form.name.data
        card_no = form.cardno.data
        card_type = 'VISA' if card_no[0] == '4' else 'MASTERCARD'
        card_exp = form.exp.data 
        card_year = form.year.data
        exisiting_card_no = query('SELECT card_no FROM card_info WHERE card_no=?', card_no)
        all_card_list = query('SELECT * FROM card_info')
        if all_card_list == []:
            all_card_list = [(0,)]
        if exisiting_card_no == []:
            cardlist = query('SELECT * FROM card_info WHERE fk_user_id=?',session['user_id'])
            for i in cardlist:
                constructAndExecuteQuery('UPDATE card_info SET "default"=? WHERE Credit_card_id=?',"False",int(i[0]))
            constructAndExecuteQuery('INSERT INTO card_info VALUES(?,?,?,?,?,?,?,?)', int(all_card_list[-1][0])+1, card_name,card_no,card_type,card_exp,card_year,session['user_id'],'True')
            return redirect(url_for('myAccount'))
        else:
            flash('Card number already exist! Please add a different card', 'danger')
            return render_template('addCard.html', form = form)
    else:
        return render_template('addCard.html', form = form)

# Edit Card route #
@app.route('/editCard', methods=['GET', 'POST'])
def editCard():
    form=PaymentInfo()
    if request.method == 'GET' :
        card_id = request.args.get('card')
        if card_id != None:
            card = query('SELECT * FROM card_info WHERE Credit_card_id=?', int(card_id))
            if card[0][6] != int(session['user_id']):
                card = []
        else:
            return redirect(url_for('home'))
        return render_template('editCard.html', form=form, card=card[0])
    if form.validate_on_submit():
        card_id = request.args.get('card')
        card = query('SELECT * FROM card_info WHERE Credit_card_id=?', int(card_id))
        edited_cardno = form.cardno.data
        edited_cardname = form.name.data 
        edited_cardtype = 'VISA' if edited_cardno[0] == '4' else 'MASTERCARD'
        edited_cardexp = form.exp.data 
        edited_cardexpyear = form.year.data
        stripped_cardno = edited_cardno.strip()
        user_existing_cards = query('SELECT * FROM card_info WHERE fk_user_id=?', session['user_id'])
        if len(user_existing_cards) == 1:
            constructAndExecuteQuery('UPDATE card_info SET card_name=?,card_no=?,exp_month=?,exp_year=?,card_type=? WHERE Credit_card_id=?',edited_cardname,edited_cardno,edited_cardexp,edited_cardexpyear,edited_cardtype,int(card_id))
            return redirect(url_for('myAccount'))
        else:
            existing_cardno = query('SELECT * FROM card_info WHERE card_no=?', stripped_cardno)
            if existing_cardno == []:
                constructAndExecuteQuery('UPDATE card_info SET card_name=?,card_no=?,exp_month=?,exp_year=?,card_type=? WHERE Credit_card_id=?',edited_cardname,edited_cardno,edited_cardexp,edited_cardexpyear,edited_cardtype,int(card_id))
                return redirect(url_for('myAccount'))
            elif existing_cardno[0][0] == int(card_id):
                constructAndExecuteQuery('UPDATE card_info SET card_name=?,card_no=?,exp_month=?,exp_year=?,card_type=? WHERE Credit_card_id=?',edited_cardname,edited_cardno,edited_cardexp,edited_cardexpyear,edited_cardtype,int(card_id))
                return redirect(url_for('myAccount'))
            else:
                flash('This card number has already been added! Please add a different card number')
                return render_template('editCard.html', form=form, card=card[0])
    else:
        card_id = request.args.get('card')
        if card_id != None:
            card = query('SELECT * FROM card_info WHERE Credit_card_id=?', int(card_id))
        else:
            return redirect(url_for('home'))
        return render_template('editCard.html', form=form, card=card[0])

# Setting Default Card route #
@app.route('/defaultCard', methods=['GET', 'POST'])
def defaultCard():
    card = request.args.get('card')
    if card == None: 
        return redirect(url_for('home'))
    try:
        cardlist = query('SELECT * FROM card_info WHERE fk_user_id=?',session['user_id'])

        for i in cardlist:
            constructAndExecuteQuery('UPDATE card_info SET "default"=? WHERE Credit_card_id=?',"False",int(i[0]))
        test = card.strip()
        constructAndExecuteQuery('UPDATE card_info SET "default"=? WHERE Credit_card_id=?',"True",int(test))
        return "[]"
    except:
        return redirect(url_for('home'))

# Remove Card route #
@app.route('/removeCard')
def removeCard():
    card = request.args.get('card')
    if card == None: 
        return redirect(url_for('myAccount'))
    try:
        test = card.strip()
        constructAndExecuteQuery('DELETE FROM card_info WHERE Credit_card_id=?', int(test))
        cardlist = query('SELECT * FROM card_info WHERE fk_user_id=?',session['user_id'])
        if cardlist != []:
            constructAndExecuteQuery('UPDATE card_info SET "default"=? WHERE Credit_card_id=?',"True",cardlist[-1][0])
        return "[]"
    except:
        return redirect(url_for('myAccount'))

# User Account route #
@app.route('/myAccount', methods=['GET', 'POST'])
def myAccount():
    form = UpdateAccountForm()
    if request.method == 'GET':
        if "user_id" not in session: 
            return redirect(url_for('home'))
        else:
            old_password = request.args.get('old')
            if old_password != None:
                current_password = query('SELECT * FROM user_accounts WHERE Id=?', session['user_id'])[0][3]
                compare_old_pw = check_password_hash(current_password, old_password)
                if not compare_old_pw:
                    return "wrong"
            user_id = session['user_id']
            user = query('SELECT * FROM user_accounts WHERE Id = ?', str(user_id))
            card_info = query('SELECT * FROM card_info WHERE fk_user_id=?', str(user_id))
            address_info = query('SELECT * from Addresses WHERE user_id=?', str(user_id))
            prev_transactions = query('SELECT * FROM prev_transactions WHERE fk_user_id=?', str(user_id))
            transactions = []
            for y in prev_transactions:
                total = 0
                for z in ast.literal_eval(y[1]):
                    total += (z[1] * z[2])
                transactions.append((y[2], str(y[3]),y[4], ast.literal_eval(y[1]), total))
    if form.validate_on_submit():
        user_id = session['user_id']
        user = query('SELECT * FROM user_accounts WHERE Id = ?', str(user_id))[0]

        card_info = query('SELECT * FROM card_info WHERE fk_user_id=?', str(user_id))
        address_info = query('SELECT * from Addresses WHERE user_id=?', str(user_id))
        new_fullname = form.fullname.data 
        new_email = form.email.data.strip()
        existing_email = query('SELECT * FROM user_accounts WHERE email=?', new_email)
        if user[2] != new_email and existing_email != []:
            flash('This email has already been added', 'danger')
            return redirect(url_for('myAccount'))
        image = request.files['image']
        filename = request.files['image'].filename   
        if filename.find('.') == -1: 
            filename = None
            bool_image = False
        else:
            bool_image = allowed_image(filename)
        if bool_image == False and filename != None:
            flash('Invalid file type for images', 'danger')
            return redirect(url_for('myAccount'))
        else: 
            if filename != None:
                image.save(os.path.join(app.config["PROFILE_UPLOADS"], filename))
                image_file = f'../static/img/profile_pic/{filename}'
                constructAndExecuteQuery('UPDATE user_accounts SET profile_image=? WHERE Id = ?', image_file, user_id)
        constructAndExecuteQuery('UPDATE user_accounts SET fullname=? WHERE Id = ?', new_fullname, user_id)
        constructAndExecuteQuery('UPDATE user_accounts SET email=? WHERE Id = ?', new_email, user_id)
        return redirect(url_for('myAccount'))
    else:
        user_id = session['user_id']
        user = query('SELECT * FROM user_accounts WHERE Id = ?', str(user_id))
        address_info = query('SELECT * from Addresses WHERE user_id=?', str(user_id))
        card_info = query('SELECT * FROM card_info WHERE fk_user_id=?', str(user_id))
        prev_transactions = query('SELECT * FROM prev_transactions WHERE fk_user_id=?', str(user_id))
        transactions = []
        for y in prev_transactions:
            total = 0
            for z in ast.literal_eval(y[1]):
                total += (z[1] * z[2])
            transactions.append((y[2], str(y[3]),y[4], ast.literal_eval(y[1]), total))
    return render_template('myAccount.html', form=form, user=user[0],credit_cards = card_info, addresses=address_info, transactions=transactions)

# Change Password route #
@app.route("/changePassword", methods=["GET", "POST"])
def changePassword():
    user = query('SELECT * FROM user_accounts WHERE Id=?', session['user_id'])[0]
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user_current_pw = form.current_password.data
        db_pw = user[3]
        compare_current_hash = check_password_hash(db_pw, user_current_pw)
        if compare_current_hash == True:
            oldpasswords = ast.literal_eval(user[6])
            for i in oldpasswords:
                if i == form.password.data:
                    flash('You cannot reuse any of your previous 5 passwords!', 'danger')
                    return render_template('changePassword.html', form=form)
            else:
                if len(oldpasswords) == 5:
                    oldpasswords = []
                    new_pw = generate_password_hash(form.password.data, 10)
                    oldpasswords.append(new_pw)
                    constructAndExecuteQuery('UPDATE user_accounts SET password=?,previous_passwords=? WHERE Id=?',new_pw,str(oldpasswords), session['user_id'])
                else:
                    new_pw = generate_password_hash(form.password.data, 10)
                    oldpasswords.append(new_pw)
                    constructAndExecuteQuery('UPDATE user_accounts SET password=?,previous_passwords=? WHERE Id=?',new_pw,str(oldpasswords), session['user_id'])
                return redirect(url_for('myAccount'))
    return render_template('changePassword.html', form=form)

# Disable account route #
@app.route("/disable", methods=["GET", "POST"])
def disable():
    form = Disable()
    if form.validate_on_submit():
        user = query('SELECT * FROM user_accounts WHERE Id=?', session['user_id'])
        if form.password.data == user[0][3]:
            constructAndExecuteQuery('UPDATE user_accounts SET account_status=? WHERE Id=?',0, session['user_id'])
            session.pop('user_id', None)
            return redirect(url_for('home'))
        else:
            flash('Password is inncorrect. Please retype your password.', 'danger')
            return redirect(url_for('disable'))
    return render_template('disable.html', form=form)

# Activate Account route#
@app.route("/activate", methods=["GET", "POST"])
def activate():
    form = Activate()
    if form.validate_on_submit():
        stripped_email = form.email.data.strip()
        user = query('SELECT * FROM user_accounts WHERE email=?', stripped_email)
        if form.password.data == user[0][3]:
            constructAndExecuteQuery('UPDATE user_accounts SET account_status=? WHERE email=?',1,stripped_email)
            session['user_id'] = user[0][0]
            return redirect(url_for('home'))
        else:
            flash('Password is inncorrect. Please retype your password.', 'danger')
            return redirect(url_for('disable'))
    return render_template('activate.html', form=form)

@app.route("/activateask", methods=["GET", "POST"])
def activateask():
        return render_template('activateask.html')

# Logout route #
@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

"""
Shop Related Routes 
"""
@app.route('/shop')
def shop():
    allProducts = query('SELECT * FROM products')
    game_list = []
    for row in allProducts:
        game_list.append(row[2])
    return render_template("shop.html",game_list=game_list,allProducts=allProducts)
@app.route('/checking',methods=['POST'])
def checking():
    data=request.form
    print(data)
    return "hello"

@app.route('/single_product/<int:id>')
def single_product(id):
    return render_template("single_product.html")

def sum_digits(digit):
            if digit < 10:
                return digit
            else:
                sum = (digit % 10) + (digit // 10)
                return sum

@app.route('/validateCardNo')
def validatecardno():
        request_xhr_key = request.headers.get('X-Requested-With')
        if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
            cc_num = request.args.get('cardno')
            # reverse the credit card number
            cc_num = cc_num[::-1]
            # convert to integer list
            cc_num = [int(x) for x in cc_num]
            # double every second digit
            doubled_second_digit_list = list()
            digits = list(enumerate(cc_num, start=1))
            for index, digit in digits:
                if index % 2 == 0:
                    doubled_second_digit_list.append(digit * 2)
                else:
                    doubled_second_digit_list.append(digit)

            # add the digits if any number is more than 9
            doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
            # sum all digits
            sum_of_digits = sum(doubled_second_digit_list)
            # return True or False
            return str(sum_of_digits % 10 == 0)


@app.route('/paymentConfirmation', methods=['GET', 'POST'])
def confirm():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
        if request.method == 'POST':
            transaction_list = []
            li = []
            bought_products = list(current_user.products)
            data = refreshAnalytics()
            data2 = refresh()
            total = 0
            for index, i in enumerate(bought_products): 
                transaction_list.append({'prod_name':i.prod_name, 'prod_quantity':i.prod_quantity, 'prod_price':i.prod_price, 'img':i.img})
                for y in data:
                    if y['name'] == i.prod_name:  
                        y['stock'] -= int(i.prod_quantity)  
                        y['count'] += int(i.prod_quantity)
                        y['amount_earned'] += (int(i.prod_quantity)*int(i.prod_price))
                for x in data2:
                    if x['prod_name'] == i.prod_name:   
                        x['stock'] -= int(i.prod_quantity)
            with open('json_files/analytics.json', 'w') as f:
                    json.dump(data, f)
            with open('json_files/product.json', 'w') as f:
                    json.dump(data2, f)
            unique = random.randint(100000000000,999999999999)
            transaction = PreviousTransactions(cartItems = str(transaction_list), transactionId = unique,transaction_date= datetime.utcnow()+timedelta(hours=8),user_id=current_user.id)
            db.session.add(transaction)
            db.session.commit()
            for i in bought_products:
                db.session.delete(i)
                db.session.commit()
            criticals.critical(f'Transaction #{unique} has been made by userID:{current_user.id}')
            print('Successful Transaction')
            global stop_threads
            stop_threads = True
    else:
        return redirect(url_for('home'))
    
@app.route('/checkout')
def checkout():
    if request.referrer == 'http://127.0.0.1:5000/userOTP':
        global stop_threads
        stop_threads = True
    elif request.referrer == 'http://localhost:5000/userOTP':
        stop_threads = True
        print(request.referrer)
    else:
        stop_threads = False
    email = query('SELECT email FROM user_accounts WHERE Id=?', session['user_id'])[0]
    fullname = query('SELECT fullname FROM user_accounts WHERE Id=?', session['user_id'])[0]
    # cartItems = query() 
    # if cartItems == []:
    #     return redirect(url_for('shop'))
    cartItems = []
    default_address = query('SELECT * FROM Addresses WHERE default_address=? AND user_id=?', "True", session['user_id'])
    default_card = query('SELECT * FROM card_info WHERE "default"=? AND fk_user_id=?', "True", session['user_id'])
    if default_address != []:
        default_address = default_address[0]
    if default_card != []:
        default_card = default_card[0]
    print(default_address, default_card)
    return render_template('checkout.html', cartItems = cartItems, address = default_address, card = default_card, fullname=fullname, email = email)

stop_threads = False
timer = 0
def tasks():
    global timer 
    timer = 600
    for i in range(600):
        global stop_threads
        if stop_threads:
            timer = 0
            print(timer)
            break 
        timer -= 1
        sleep(1)
        print(timer)

@app.route('/otp', methods=['GET', 'POST'])
def enter_otp():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
        global stop_threads
        stop_threads = False
        global otp
        if request.method == 'GET':
            email = query('SELECT email FROM user_accounts WHERE Id=?', session['user_id'])[0][0]
            fullname = query('SELECT fullname FROM user_accounts WHERE Id=?', session['user_id'])[0][0]
            otp =  send_qr_code(email, fullname)
            threading.Thread(target=tasks).start()
            return redirect(url_for('u'))
        if request.method == 'POST':
            user_otp = request.args.get('otp')
            if timer == 0:
                otp = ''
            if otp == '':
                return "expired"
            elif int(user_otp) ==  otp:
                return "successful"
            else:
                return "wrong"
    else:
        return redirect(url_for('home'))

@app.route('/userOTP')
def u():
    return render_template('otp.html')


"""
Admin Related Routes
"""

# Admin Home Page #
@app.route('/admin')
def admin():
    # previousTransaction = PreviousTransactions.query.all()
    previousTransaction = query('SELECT * FROM prev_transactions')
    # previousTransaction =[]
    # li = []
    for i in previousTransaction: 
        if i[4] == 'Awaiting order':
            li.append(i)
    number = len(previousTransaction)
    return render_template('admin/admin.html', previousTransaction = previousTransaction, number = number)

# Admin Analytics Page #    
@app.route('/adminAnalytics')
def analytics():
    data = refreshAnalytics()
    return render_template('admin/adminAnalytics.html', data = data)

@app.route('/stats')
def stats():
    data = refreshAnalytics()
    return jsonify(data)

@app.route('/downloadcsvs')
def downloadcsv():
    data = refreshAnalytics()
    return send_csv(data,"data.csv", ["id", "name","stock","count","amount_earned"])

@app.route('/trans')
def trans():
    previous_transactions = query('SELECT * FROM prev_transactions')
    transactions = []
    for y in previous_transactions:
        total = 0
        for z in ast.literal_eval(y[1]):
            total += (z[1] * z[2])
        transactions.append((y[2], str(y[3]),y[4], ast.literal_eval(y[1]), y[-1],total))
    return render_template('admin/adminTranList.html', trans = transactions)

@app.route('/adminIndvTran')
def indv():
    id = request.args.get('id')
    previous_transactions = query('SELECT * FROM prev_transactions WHERE transactionid=?', id)
    transactions = []
    for y in previous_transactions:
        total = 0
        for z in ast.literal_eval(y[1]):
            total += (z[1] * z[2])
        transactions.append((y[2], str(y[3]),y[4], ast.literal_eval(y[1]), y[-1],total))
    return render_template('admin/adminTransactions.html', trans = transactions)

@app.route('/Calendar')
def Calander():
    if request.method == 'GET':
        name = request.args.get('ename')
        description = request.args.get('edesc')
        date = request.args.get('edate')
        className = request.args.get('ecolor')
        icon = request.args.get('eicon')
        new_dict = {
        "title": name,
        "description": description,
        "start": date,
        "end": date,
        "className": className,
        "icon" : icon
        }
        if name == None:
            pass
        else:
            with open('json_files/events.json', 'r') as f:
                data = json.load(f)
                data.append(new_dict)
            with open('json_files/events.json', 'w') as f:
                json.dump(data, f)
    return render_template('admin/calander.html')

@app.route('/Logs')
def Logs():
    errors_logs = []
    with open('errors.log') as f: 
        line = f.readlines()
        for i in line:
            dic = {}
            splitted = i.split(' ')
            dic["date"] = splitted[0]
            dic["time"] = splitted[1]
            dic["error"] = splitted[2]+ " " + splitted[3]
            sentence = ""
            for i in range(4, len(splitted)-2):
                sentence += f"{splitted[i]} "
            eddited = sentence.replace('\n', '')
            dic["message"] = eddited
            routepos = splitted[-2].index(':')
            sen = ""
            for i in range(routepos+1, len(splitted[-2])):
                sen += splitted[-2][i]
            idpos = splitted[-1].index(':')
            sens = ""
            for i in range(idpos+1, len(splitted[-1])):
                sens += splitted[-1][i]
            dic["id"] = sens
            dic["route"] = sen
            errors_logs.append(dic)
    info_logs =[]
    with open('infos.log') as f: 
        line = f.readlines()
        for i in line:
            dicd = {}
            splitted = i.split()
            dicd["date"] = splitted[0]
            dicd["time"] = splitted[1]
            dicd["error"] = splitted[2]
            dicd["email"] = splitted[3]
            sentence = ""
            for i in range(4, len(splitted)):
                sentence += f"{splitted[i]} "
            eddited = sentence.replace('\n', '')
            dicd["message"] = eddited
            info_logs.append(dicd)
    with open('criticals.log', 'r+') as f: 
        lines = f.readlines()
        critical_logs = []
        for i in lines:
            splitted = i.split()
            dicdd = {}
            dicdd["date"] = splitted[0]
            dicdd["time"] = splitted[1]
            dicdd["error"] = splitted[2]
            dicdd["transaction_id"] = splitted[4]
            pos = splitted[-1].index(":")
            user_id = ""
            for i in range(pos+1, len(splitted[-1])): 
                user_id += splitted[-1][i]
            edited = user_id.replace('\n', '')
            dicdd["user_id"] = user_id
            sentence = ""
            for i in range(3, len(splitted)):
                sentence += f"{splitted[i]} "
            eddited = sentence.replace('\n', '')
            dicdd["message"] = eddited
            critical_logs.append(dicdd)
    return render_template('admin/adminlogs.html', errors=errors_logs, info=info_logs, criticals = critical_logs)

@app.route('/announcement')
def announcement():
    if request.method == 'GET':
            name = request.args.get('ann_ename')
            if name == '':
                return redirect(url_for('Calander'))
            description = request.args.get('anouncements')
            desc = request.args.get('edesc_ann')
            start_date = request.args.get('edateStart')
            end_date = request.args.get('edateEnd')
            className = request.args.get('ecolor_ann')
            icon = request.args.get('eicon_ann')
            new_dict = {
            "title": name,
            "anouncement": description,
            "description":desc,
            "start": start_date,
            "end": end_date,
            "className": className,
            "icon" : icon
            }
            if name == None:
                pass
            else:
                with open('json_files/events.json', 'r') as f:
                    data = json.load(f)
                    data.append(new_dict)
                with open('json_files/events.json', 'w') as f:
                    json.dump(data, f)
    return redirect(url_for('Calander'))

@app.route('/events')
def events():
    data = refreshEvents()
    return jsonify(data)

## Admin User Section Routes##
@app.route('/viewIndividualUser', methods=['GET', 'POST'])
def viewIndividualUser():
        id = request.args.get('id')
        # user = query)
        user = query('SELECT * FROM user_accounts WHERE Id=?', id)[0]
        previous_transactions = query('SELECT * FROM prev_transactions WHERE fk_user_id=?', id)
        reviews = []
        transactions = []
        for y in previous_transactions:
            total = 0
            for z in ast.literal_eval(y[1]):
                total += (z[1] * z[2])
            transactions.append((y[2], str(y[3]),y[4], ast.literal_eval(y[1]), total))
        return render_template('admin/viewIndividualUser.html', user=user, reviews=reviews, previous_transactions = transactions)

@app.route('/orderStatus', methods=['GET', 'POST'])
def orderStatus():
    if request.method == 'GET':
        id = request.args.get('id')
        previous_transactions = query('SELECT * FROM prev_transactions WHERE transactionid=?', id)
        transactions = []
        for y in previous_transactions:
            total = 0
            for z in ast.literal_eval(y[1]):
                total += (z[1] * z[2])
            transactions.append((y[2], str(y[3]),y[4], ast.literal_eval(y[1]), y[-1],total))
        return render_template('admin/orderStatus.html', transaction=transactions)
    else:
        option = request.form['options']
        id = request.args.get('id')
        constructAndExecuteQuery('UPDATE prev_transactions SET transaction_status = ?  WHERE transactionid = ?', option, id)
        return redirect(url_for('admin'))

@app.route('/listUser')
def listUser():
    users = query('SELECT * FROM user_accounts')
    return render_template('admin/usersList.html', users = users)

""" Admin E-commerce Section Routes """

# Admin view all games route #
@app.route('/productList')
def productList():
    data = query('SELECT * FROM products')
    return render_template('admin/productList.html', data = data)

# Admin view game route #
@app.route('/adminViewproduct', methods=['GET', 'POST'])
def viewProduct():
    id = request.args.get('id')
    product = query('SELECT * FROM products WHERE prod_id=?',int(id))[0]
    review = None 
    analytics = None
    num = int(id)
    return render_template('admin/productDetail.html', product= product, review = review, analytics = analytics, num=num)

# Admin add game route #
@app.route('/adminAddproduct', methods=['GET', 'POST'])
def adminAdd():
    form = AdminAddProductForm()
    if request.method == "POST":
        latest_id = query('SELECT * FROM PRODUCTS')[-1][0]
        image = request.files['image']
        filename = request.files['image'].filename
        new_product_name = form.name.data
        new_product_price = form.price.data
        new_product_description = form.description.data
        new_product_id = form.id.data
        new_game_genre = form.genre.data
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
        image_file = f'../static/img/product_img/{filename}' 
        constructAndExecuteQuery('INSERT INTO products(prod_id, prod_name,prod_quantity, prod_price,prod_desc,prod_img,genre1) VALUES(?,?,?,?,?,?,?)', int(new_product_id),new_product_name, 100,float(new_product_price), new_product_description,image_file, new_game_genre)
        return redirect(url_for('productList'))
    else:
        latest_id = query('SELECT * FROM PRODUCTS')[-1][0]
    return render_template('admin/adminAddProduct.html', latest_id = int(latest_id)+1, form=form)

# Admin update game route #
@app.route('/adminUpdateproduct', methods=['POST', 'GET'])
def update():
    form = AdminUpdateProductForm()
    productId = request.args.get('id')
    if request.method == 'POST':
        item_id = form.id.data
        item_name = form.name.data 
        item_desc = form.description.data
        item_price = form.price.data
        image = request.files['image']
        filename = request.files['image'].filename 
        if filename.find('.') == -1: 
            filename = None
            bool_image = False
        else:
            bool_image = allowed_image(filename)
        if bool_image == False and filename != None:
            flash('Invalid file type for images', 'danger')
            return redirect(request.referrer)
        else: 
            if filename != None:
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                image_file = f'../static/img/product_img/{filename}'    
                constructAndExecuteQuery('UPDATE products SET prod_name=?,prod_desc=?,prod_price=?,prod_img=? WHERE prod_id=?', item_name, item_desc,float(item_price), image_file, int(productId))
                return redirect(url_for('productList'))
        constructAndExecuteQuery('UPDATE products SET prod_name=?,prod_desc=?,prod_price=? WHERE prod_id=?', item_name, item_desc,float(item_price), int(productId))
        return redirect(url_for('productList'))
    else:
        product = query('SELECT * FROM products WHERE prod_id=?',int(productId))[0]
        return render_template('admin/adminUpdateProduct.html', product = product, form=form)

# Admin add stock route #
@app.route('/addStock', methods=['POST', 'GET'])
def stock():
    if request.method == 'GET':
        productId = request.args.get('id')
        product = query('SELECT * FROM products WHERE prod_id=?',int(productId))[0]
        return render_template('admin/adminStock.html', data = product)
    else:
        productId = request.args.get('id')
        cun = request.form['quant[1]']
        orginal = query('SELECT prod_quantity FROM products WHERE prod_id=?', int(productId))[0][0]
        constructAndExecuteQuery('UPDATE products SET prod_quantity=? WHERE prod_id=?', orginal + int(cun), int(productId))
        return redirect(url_for('admin'))

# Admin delete game route #
@app.route('/delete', methods=['POST', 'GET'])
def delete():
    form = AdminUpdateProductForm()
    productId = request.args.get('id')
    if request.method == 'POST':
        product = constructAndExecuteQuery('DELETE FROM products WHERE prod_id=?', int(productId))
        return redirect(url_for('admin'))
    else:
        product = query('SELECT * FROM products WHERE prod_id=?', int(productId))[0]
        return render_template('admin/adminDeleteProduct.html', product=product, form=form)

"""Reset Password token routes"""

# Send email to user to reset password route #
def send_reset_email(user):
    s = Serializer(current_app.config['SECRET_KEY'], 600)
    token =s.dumps({'user_id': user[0]}).decode('utf-8')
    msg = Message('Password Reset Request', sender='testemailnyp@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

# Reset password route #
@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    form = RequestResetForm()
    if "attempts" not in session:
        session['attempts'] = 5
    if "user_id" in session:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        email = form.email.data.strip()
        user = query('SELECT * FROM user_accounts WHERE email=?',email)[0]
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

# Reset password with token route #
@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    form = ResetPasswordForm()
    if "user_id" in session: 
        return redirect(url_for('home'))
    user = verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'danger')
        return redirect(url_for('reset_request'))
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, 10)
        db_pw = user[3]
        oldpasswords = ast.literal_eval(user[6])
        for i in oldpasswords:
            if i == hashed_password:
                flash('You cannot reuse any of your previous 5 passwords!', 'danger')
                return redirect(request.referrer)
        else:
            if len(oldpasswords) == 5:
                oldpasswords = []
                new_pw = generate_password_hash(form.password.data, 10)
                oldpasswords.append(new_pw)
                constructAndExecuteQuery('UPDATE user_accounts SET password=?,previous_passwords=? WHERE Id=?',new_pw,str(oldpasswords), user[0])
            else:
                new_pw = generate_password_hash(form.password.data, 10)
                oldpasswords.append(new_pw)
                constructAndExecuteQuery('UPDATE user_accounts SET password=?,previous_passwords=? WHERE Id=?',new_pw,str(oldpasswords), user[0])
            flash('Your password has been updated! You are now able to log in', 'success')
            session['attempts'] = 5
            return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

"""Error Handling Routes"""

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    print(request.base_url)
    try:
        userid = current_user.id
    except:
        userid = "guest"
    errors.error(f"{e} Route:{request.base_url} userID:{userid}")
    return render_template('pageNotFound.html'), 404

@app.errorhandler(500)
def page_not_found500(x):
    errors.error(f"{x}")
    return render_template('feedbackError.html'), 500


