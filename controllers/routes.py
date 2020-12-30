"""
All dynamic routing belongs here 
"""

import os, json, ast, random
from flask import render_template, redirect, flash, url_for, request, jsonify, Request, send_file, make_response, session, abort
from flask_login import current_user, login_user, logout_user, login_required
from controllers import app, db, bcrypt, mail
from controllers.forms import RegistrationForm, LoginForm, Billing, PaymentInfo, ContactUsForm, PasswordForm, Disable, Activate, ChangePasswordForm
from controllers.forms import RegistrationForm, LoginForm, AdminAddProductForm, AdminUpdateProductForm, UpdateAccountForm, UpdateBilling, RequestResetForm, ResetPasswordForm, UpdateCard
from controllers.Sentemail import sendEmail, adminEmail
from controllers.models import User, Product, CardInfo, AddressInfo, PreviousTransactions, Review, ProductReview
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_mail import Message
from flask import Flask
from cryptography.fernet import Fernet
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

cipher_suite = Fernet(key)
vali = current_user


"""
Functions 
"""

##Refreshes the json file if admin adds a new product in##
def refresh():
    with open('json_files/product.json', 'r+') as f:
        data = json.load(f)
    return data 

def refreshEvents():
    with open('json_files/events.json', 'r+') as f:
        data = json.load(f)
    return data

def refreshAnalytics():
    with open('json_files/analytics.json', 'r+') as f:
        data = json.load(f)
    return data 


##Ensures that allowed images are accepted##
def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    print(filename)
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/qr')
def qr():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
        email = current_user.email
        fullname = current_user.fullname
        global otp
        otp = send_qr_code(email, fullname)
        threading.Thread(target=tasks).start()
        return str(otp)
    else: 
        return redirect(url_for('home'))

"""
Home, contact-us, about pages 
"""

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/contactUs', methods=['GET', 'POST'])
def contactUs():
    form = ContactUsForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for("homepage"))
    return render_template("contactUs.html", form=form)

@app.route('/terms')
def terms(): 
    return render_template('terms.html')

"""
ERROR ROUTE
"""
"""
Account Related Routes 
"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('registerStep2'))
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        name = form.fullname.data
        email = form.email.data
        previousPass = []
        previousPass.append(hashed_password)
        user = User(fullname=name, email=email, password=hashed_password, previousPasswords = str(previousPass), isAdmin = 'False')
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/registerStep2', methods=['GET', 'POST'])
def registerStep2():
    form = Billing()
    existing = AddressInfo.query.filter_by(user_id=current_user.id)
    if form.validate_on_submit():
        exisr = AddressInfo.query.filter_by(address=form.address.data, user_id=current_user.id).first()
        print(exisr)
        if exisr == None:
            for i in existing:
                i.default = 'False'
            address = form.address.data.strip()
            country = form.country.data
            state = form.state.data.strip()
            postal = form.postal.data
            address = AddressInfo(address=address, country=country, state=state, postal=postal, user_id = current_user.id, default='True')
            db.session.add(address)
            db.session.commit()
            return redirect(url_for('myAccount'))
        elif str(exisr).find('SELECT') != None and exisr == None:
            for i in existing:
                i.default = 'False'
            address = form.address.data.en
            country = form.country.data
            state = form.state.data
            postal = form.postal.data
            address = AddressInfo(address=address, country=country, state=state, postal=postal, user_id = current_user.id, default='True')
            db.session.add(address)
            db.session.commit()
            return redirect(url_for('myAccount'))
        else:
            flash('Address already added! Please add a different address', 'danger')
    return render_template('registerStep2.html', form = form, data=[])

@app.route('/editAddress', methods=['GET', 'POST'])
def editBilling():
    address = request.args.get('address')
    addressinfo = AddressInfo.query.filter_by(address=address, user_id=current_user.id).first()
    address = addressinfo.address.strip()
    country = addressinfo.country
    state = addressinfo.state.strip()
    postal = addressinfo.postal
    data = {"address":address, "country":country, "state":state, "postal":postal, "default":addressinfo.default}
    form = UpdateBilling()
    if request.method == 'GET':
        form.country.data = country
    if form.validate_on_submit() and request.method=='POST':
        exisr = AddressInfo.query.filter_by(address=form.address.data, user_id=current_user.id).first()
        print(exisr)
        if exisr == None:
            addressinfo.address = form.address.data
            addressinfo.country = form.country.data
            addressinfo.state = form.state.data
            addressinfo.postal = form.postal.data
            db.session.commit()
            return redirect(url_for('myAccount'))
        elif addressinfo.address == form.address.data:
            print(form.country.data)
            addressinfo.address = form.address.data
            addressinfo.country = form.country.data
            addressinfo.state = form.state.data
            addressinfo.postal = form.postal.data
            db.session.commit()
            return redirect(url_for('myAccount'))
        else:
            flash('Address already added! Please add a different address', 'danger')
            return render_template('editAddress.html', form=form, data = addressinfo)
    return render_template('editAddress.html', form=form, data = data)
    
@app.route('/editCardInfo', methods=['GET', 'POST'])
def editCardInfo():
    cardno1 = request.args.get('card')
    id = request.args.get('id')
    cards = CardInfo.query.all()
    for i in cards:
        cardnum = cipher_suite.decrypt(i.cardno)
        cardn = str(cardnum)
        cardnss = cardn[1:]
        cardns = cardnss[1:-1]
        iteration = i
        if cardns == cardno1:
            card_name = i.card_name
            exp = i.exp
            year = i.year
            cardo = {'id':i.id,'card_name':card_name, 'cardno':cardns, 'exp':exp, 'year':year}
            break 
    form = UpdateCard()
    if form.validate_on_submit():
        cardno = form.cardno.data
        print(cardno)
        for i in cards:
            cardnum = cipher_suite.decrypt(i.cardno)
            cardn = str(cardnum)
            cardnss = cardn[1:]
            cardns = cardnss[1:-1]
            print(cardns)
            if cardns == cardno:
                cardnsss = cardns
                iteration = i
                card_name = i.card_name
                exp = i.exp
                year = i.year
                card = {'id':i.id,'card_name':card_name, 'cardno':cardns, 'exp':exp, 'year':year}
                print(card)
                break
            else:
                cardnsss = None
                card = cardo
        print(cardnss)
        print(id)
        if card['id'] == int(id) and card['cardno'] == cardnsss:
            print('editing orginal card')
            iteration.card_name = form.name.data
            d = bytes(form.cardno.data, encoding='utf8')
            encoded_text = cipher_suite.encrypt(d)
            iteration.cardno = encoded_text
            iteration.exp = form.exp.data
            iteration.year =  form.year.data
            if cardno[0] == '5':
                iteration.card_type = "master"
                print('master')
            elif cardno[0] == '4':
                iteration.card_type = "visa"
            db.session.commit()
            return redirect(url_for('myAccount'))
        elif card['cardno'] == cardnsss and card['id'] != int(id):
            print('error')
            flash('Card number already exist! Please add a different card', 'danger')
            return render_template('editCard.html', form=form, data = cardo)
        else:
            iteration.card_name = form.name.data
            d = bytes(form.cardno.data, encoding='utf8')
            encoded_text = cipher_suite.encrypt(d)
            iteration.cardno = encoded_text
            iteration.exp = form.exp.data
            iteration.year = form.year.data
            if cardno[0] == '5':
                iteration.card_type = "master"
            else:
                iteration.card_type = "visa"
            db.session.commit()
            return redirect(url_for('myAccount'))
    return render_template('editCard.html', form=form, data = cardo)

@app.route('/registerStep3', methods=['GET', 'POST'])
def registerStep3():
    form = PaymentInfo()
    if form.validate_on_submit():
        msg = form.cardno.data
        cards = CardInfo.query.all()
        for i in cards:
            cardnum = cipher_suite.decrypt(i.cardno)
            cardn = str(cardnum)
            cardnss = cardn[1:]
            cardns = cardnss[1:-1]
            iteration = i
            print(cardns, iteration)
            if cardns == msg:
                flash('Card number already exist! Please add a different card', 'danger')
                return render_template('registerStep3.html', form = form, data = None)
        else:
            card_no = form.cardno.data
            if card_no[0] == '5':
                card_type = "master"
            elif card_no[0] == "4":
                card_type = "visa"
            cardnses = CardInfo.query.filter_by(user_id=current_user.id)
            for i in cardnses: 
                i.default = 'False'
            msg = form.cardno.data
            cards = CardInfo.query.all()
            for i in cards:
                cardnum = cipher_suite.decrypt(i.cardno)
                cardn = str(cardnum)
                cardnss = cardn[1:]
                cardns = cardnss[1:-1]
                iteration = i
                if cardns == msg:
                    return render_template('registerStep3.html', form = form, data = None)
            else:
                print(current_user.id)
                cardnses = CardInfo.query.filter_by(user_id=current_user.id)
                print(cardnses)
                if str(cardnses).find('SELECT') != None:
                    cardns = []
                card_no = form.cardno.data
                if card_no[0] == '5':
                    card_type = "master"
                else:
                    card_type = "visa"
                for i in cardnses: 
                    i.default = 'False'
                msg = form.cardno.data
                d = bytes(msg, encoding='utf8')
                encoded_text = cipher_suite.encrypt(d)
                cardinfo = CardInfo(card_name=form.name.data, cardno=encoded_text, exp=form.exp.data, year=form.year.data, user_id = current_user.id, card_type = card_type, default='True')
                db.session.add(cardinfo)
                db.session.commit()
                return redirect(url_for('myAccount'))
    return render_template('registerStep3.html', form = form, data = None)

lock_timer = 0
def task():
    global lock_timer 
    lock_timer = 300
    for i in range(300):
        lock_timer -= 1
        sleep(1)
        print(lock_timer)
    print('finished')

def emailTask():
    global email
    print(email)
    with app.app_context():
        adminEmail(email)
    return "sent"

@app.route('/timer')
def timerr():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest': 
        global timer
        print("actual", timer)
        return str(timer)
    else:
        return redirect(url_for('home'))

@app.route('/lock_timer')
def lock_timerr():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest': 
        global lock_timer
        print(lock_timer)
        return str(lock_timer)
    else:
        return redirect(url_for('home'))

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
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user == None: 
            flash('Please check your credentials again', 'danger')
            return render_template('login.html', form=form)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print(user.active)
            if user.active == "Inactive":
                return redirect(url_for('activateask'))
            login_user(user, remember=form.remember.data)
            email = user.email
            infos.info('%s logged in successfully', email)
            session['attempts'] = 5
            return redirect(url_for('home'))
        else:
            email = user.email
            infos.info('%s failed to log in', email)
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
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                if user.active == "Inactive":
                    return redirect(url_for('activateask'))
                login_user(user, remember=form.remember.data)
                if user.email == 'admin@gmail.com':
                    return redirect(url_for('admin'))
                else:
                    return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        return render_template('login.html', title='Login', form=form)


@app.route('/checkPassword')
def checkpassword():
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
        datas = {"data":[]}
        password = request.args.get('pass')
        print(password)
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

@app.route('/myAccount', methods=['GET', 'POST'])
@login_required
def myAccount():
    name =current_user.fullname
    email = current_user.email
    removeConfirmation = request.args.get('delete')
    removeAddress = request.args.get('address')
    removeCard = request.args.get('card')
    removeReview = request.args.get('name')
    if removeAddress != None and removeConfirmation == 'true':
        addresses = AddressInfo.query.filter_by(user_id=current_user.id)
        address = AddressInfo.query.filter_by(address=removeAddress, user_id = current_user.id).first()
        db.session.delete(address)
        db.session.commit()
        addresses[-1].default = 'True'
        db.session.commit()
    elif removeReview != None and removeConfirmation == 'true': 
        review = Review.query.filter_by(prod_name=removeReview, user_id=current_user.id).first()
        db.session.delete(review)
        db.session.commit()
    elif removeCard != None and removeConfirmation == 'true':
        cards = CardInfo.query.filter_by(user_id=current_user.id)
        for i in cards:
            cardnum = cipher_suite.decrypt(i.cardno)
            cardn = str(cardnum)
            cardnss = cardn[1:]
            cardns = cardnss[1:-1]
            if cardns == removeCard:
                card = i
                break 
        db.session.delete(card)
        db.session.commit()
        cards[-1].default = 'True'
        db.session.commit()
    form = UpdateAccountForm()
    if form.validate_on_submit():
        image = request.files['image']
        filename = request.files['image'].filename   
        if filename.find('.') == -1: 
            filename = None
            bool_image = False
        else:
            bool_image = allowed_image(filename)
        print(filename)
        if bool_image == False and filename != None:
            flash('Invalid file type for images', 'danger')
            return redirect(url_for('myAccount'))
        else: 
            if filename != None:
                image.save(os.path.join(app.config["PROFILE_UPLOADS"], filename))
                current_user.image_file = f'../static/img/profile_pic/{filename}'
            current_user.fullname = form.fullname.data
            current_user.email = form.email.data
            db.session.commit()
            flash('Your account has been updated!', 'success')
            return redirect(url_for('myAccount'))
    old = request.args.get('old')
    new = request.args.get('new')
    if old != None:
        old_password = current_user.password
        if bcrypt.check_password_hash(current_user.password, old):
            pass
        else:
            return "wrong"
    if new != None:
        hashed_password = bcrypt.generate_password_hash(new).decode('utf-8')
        current_user.password = hashed_password
        return redirect(url_for('myAccount'))
    elif request.method == 'GET':
        tran_list = []
        card_list = []
        form.fullname.data = current_user.fullname
        form.email.data = current_user.email
        image_file = current_user.image_file
        address = current_user.address_info
        cards = current_user.card_info
        for i in cards:
            cardnum = cipher_suite.decrypt(i.cardno)
            cardn = str(cardnum)
            cardnss = cardn[1:]
            cardns = cardnss[1:-1]
            card_name = i.card_name
            exp = i.exp
            year = i.year
            card_list.append({'id':i.id,'card_name':card_name, 'cardno':cardns, 'exp':exp, 'year':year, "card_type":i.card_type, "default":i.default})
        previous_transactions = current_user.previousTransactions 
        reviews = current_user.review 
        for i in previous_transactions:
            total = 0
            date = i.transaction_date
            items = ast.literal_eval(i.cartItems)
            for j in items:
                total += int(j['prod_price']*j['prod_quantity'])
            tran_list.append({'id':i.transactionId, 'total':total ,'date': str(date), 'status': i.status,'items':ast.literal_eval(i.cartItems)})
    tran_list = []
    card_list = []
    address_list = []
    image_file = current_user.image_file
    address = current_user.address_info
    cards = current_user.card_info
    for addressinfo in address:
        addresss = addressinfo.address
        country = addressinfo.country
        state = addressinfo.state
        postal = addressinfo.postal
        data = {"address":addresss, "country":country, "state":state, "postal":postal, "default":addressinfo.default}
        address_list.append(data)
    for i in cards:
        cardnum = cipher_suite.decrypt(i.cardno)
        cardn = str(cardnum)
        cardnss = cardn[1:]
        cardns = cardnss[1:-1]
        card_name = i.card_name
        exp = i.exp
        year = i.year
        card_list.append({'id':i.id,'card_name':card_name, 'cardno':cardns, 'exp':exp, 'year':year, "card_type":i.card_type, "default":i.default})
    previous_transactions = current_user.previousTransactions 
    reviews = current_user.review 
    for i in previous_transactions:
        total = 0
        date = i.transaction_date
        items = ast.literal_eval(i.cartItems)
        for j in items:
            total += int(j['prod_price']*j['prod_quantity'])
        tran_list.append({'id':i.transactionId, 'total':total ,'date': str(date), 'status': i.status,'items':ast.literal_eval(i.cartItems)})        
    return render_template('myAccount.html', title='Account', image_file=image_file, form=form, accountInfo = address_list, previous_transactions = tran_list, review=reviews, card=card_list, name=name, email=email)

@app.route("/changePassword", methods=["GET", "POST"])
def changePassword():
    user = current_user
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if user and bcrypt.check_password_hash(user.password, form.current_password.data):
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            oldpassowrds = ast.literal_eval(current_user.previousPasswords)
            for i in oldpassowrds:
                if bcrypt.check_password_hash(i, form.password.data):
                    print('old password')
                    flash('You cannot reuse any of your previous 5 passwords!', 'danger')
                    return render_template('changePassword.html', form=form)
            else:
                if len(oldpassowrds) == 5:
                    oldpassowrds = []
                    oldpassowrds.append(hashed_password)
                    current_user.password = hashed_password
                    current_user.previousPasswords = str(oldpassowrds)
                    db.session.commit()
                else:    
                    oldpassowrds.append(hashed_password)
                    current_user.password = hashed_password
                    current_user.previousPasswords = str(oldpassowrds)
                    db.session.commit()
                return redirect(url_for('myAccount'))
    return render_template('changePassword.html', form=form)


@app.route("/disable", methods=["GET", "POST"])
def disable():
    # user = current_user
    # try: 
    #     email = current_user.email
    # except:
    #     return redirect(url_for('login'))
    # form = Disable()
    # if form.validate_on_submit():
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         current_user.active = "Inactive"
    #         db.session.commit()
    #         logout_user()
    #         return redirect(url_for('home'))
    #     else:
    #         flash('Password is inncorrect. Please retype your password.', 'danger')
    #         return redirect(url_for('disable'))
    return render_template('disable.html', form=form)

@app.route("/activate", methods=["GET", "POST"])
def activate():
        form = Activate()
        # if form.validate_on_submit():
        #     user = User.query.filter_by(email=form.email.data).first()
        #     if user and bcrypt.check_password_hash(user.password, form.password.data):
        #         login_user(user)
        #         user.active = "Active"
        #         db.session.commit()
        #         return redirect(url_for('home'))
        #     else:
        #         flash('Password is inncorrect. Please retype your password.', 'danger')
        #         return redirect(url_for('activate'))
        return render_template('activate.html', form=form)

@app.route("/activateask", methods=["GET", "POST"])
def activateask():
        return render_template('activateask.html')

# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for('home'))

@app.route('/defaultAddress', methods=['GET', 'POST'])
def defaultAddress():
    address = request.args.get('address')
    if address == None:
        return redirect(url_for('home'))
    try:
        addressList = AddressInfo.query.filter_by(user_id= current_user.id)
        for i in addressList:
            i.default = 'False'
        DefaultAdd = AddressInfo.query.filter_by(address=address, user_id=current_user.id).first()
        DefaultAdd.default = 'True'
        db.session.commit()
    except:
        return redirect(url_for('home'))

@app.route('/defaultCard', methods=['GET', 'POST'])
def defaultCard():
    card = request.args.get('card')
    if card == None: 
        return redirect(url_for('home'))
    try:
        cardList = CardInfo.query.filter_by(user_id= current_user.id)
        for i in cardList:
            print(i)
            i.default = 'False'
            cardnum = cipher_suite.decrypt(i.cardno)
            cardn = str(cardnum)
            cardnss = cardn[1:]
            cardns = cardnss[1:-1]
            if cardns == card:
                iteration = i
                print(iteration)
        iteration.default = 'True'
        db.session.commit()
    except:
        return redirect(url_for('home'))

"""
Shop Related Routes 
"""
@app.route('/shop')
def shop():
    return render_template("shop.html")

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
    print(request.referrer)
    if request.referrer == 'http://127.0.0.1:5000/userOTP':
        global stop_threads
        stop_threads = True
        print(request.referrer)
    elif  request.referrer == 'http://localhost:5000/userOTP':
        stop_threads = True
        print(request.referrer)
    else:
        stop_threads = False
    try:
        email = current_user.email
    except:
        return redirect(url_for('shop'))
    fullname = current_user.fullname
    card = None
    cartItems = current_user.products 
    if cartItems == []:
        return redirect(url_for('shop'))
    cardinfo = CardInfo.query.filter_by(user_id=current_user.id, default='True').first()
    print(cardinfo)
    try:
        cardnum = cipher_suite.decrypt(cardinfo.cardno)
        cardn = str(cardnum)
        cardnss = cardn[1:]
        cardns = cardnss[1:-1]
        card = {'card_name':cardinfo.card_name, 'cardno':cardns, 'exp':cardinfo.exp, 'year':cardinfo.year}
    except:
        pass
    address_info = AddressInfo.query.filter_by(user_id=current_user.id, default='True').first()
    print(address_info)
    if address_info == None:
        country = 'Singapore'
    else:
        country = address_info.country
    return render_template('checkout.html', cartItems = cartItems, address = address_info, card = card, fullname=fullname, email = email, country = country)

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
            email = current_user.email
            fullname = current_user.fullname
            otp =  send_qr_code(email, fullname)
            threading.Thread(target=tasks).start()
            return redirect(url_for('u'))
        if request.method == 'POST':
            user_otp = request.args.get('otp')
            if timer == 0:
                otp = ''
            if otp == '':
                print("expired ")
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

## Admin Static Routes ##
@app.route('/admin')
def admin():
    # previousTransaction = PreviousTransactions.query.all()
    previousTransaction =[]
    li = []
    # for i in previousTransaction: 
    #     if i.status == 'Awaiting order':
    #         li.append(i)
    number = len(li)
    return render_template('admin/admin.html', previousTransaction = previousTransaction, number = number)


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
    if current_user.email == 'admin@gmail.com':
        transactions = PreviousTransactions.query.all()
        tran_list = []
        for i in transactions:
            total = 0
            date = i.transaction_date
            items = ast.literal_eval(i.cartItems)
            for j in items:
                total += int(j['prod_price']*j['prod_quantity'])
            tran_list.append({'user_id':i.user_id,'id':i.transactionId, 'total':total ,'date': str(date), 'status': i.status,'items':ast.literal_eval(i.cartItems)})
        return render_template('admin/adminTranList.html', trans = tran_list)

@app.route('/adminIndvTran')
def indv():
    id = request.args.get('id')
    trans = PreviousTransactions.query.filter_by(transactionId=id).first()
    transactions = []
    transactions.append(trans)
    tran_list = []
    for i in transactions:
        total = 0
        date = i.transaction_date
        items = ast.literal_eval(i.cartItems)
        for j in items:
            total += int(j['prod_price']*j['prod_quantity'])
        tran_list.append({'user_id':i.user_id,'id':i.transactionId, 'total':total ,'date': str(date), 'status': i.status,'items':ast.literal_eval(i.cartItems)})
    return render_template('admin/adminTransactions.html', trans = tran_list)

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
            print(splitted)
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
@app.route('/viewUser')
def viewUser():
    try:
        if current_user.email == 'admin@gmail.com':
            return render_template('admin/viewUser.html')
    except:
        return redirect(url_for('home'))

@app.route('/viewIndividualUser', methods=['GET', 'POST'])
def viewIndividualUser():
        id = request.args.get('id')
        user = User.query.filter_by(id=int(id)).first()
        address = user.address_info
        reviews = user.review 
        previous_transactions = user.previousTransactions
        tran_list = []
        for i in previous_transactions:
            total = 0
            date = i.transaction_date
            items = ast.literal_eval(i.cartItems)
            for j in items:
                total += int(j['prod_price']*j['prod_quantity'])
            tran_list.append({'id':i.transactionId, 'total':total ,'date': str(date), 'status': i.status,'items':ast.literal_eval(i.cartItems)})
        return render_template('admin/viewIndividualUser.html', user=user, address=address, reviews=reviews, previous_transactions = tran_list)

@app.route('/orderStatus', methods=['GET', 'POST'])
def orderStatus():
    if request.method == 'GET':
        id = request.args.get('id')
        transaction = PreviousTransactions.query.filter_by(transactionId=id).first()
        return render_template('admin/orderStatus.html', transaction=transaction)
    else:
        option = request.form['options']
        id = request.form['id']
        transaction = PreviousTransactions.query.filter_by(transactionId=id).first()
        transaction.status = option
        db.session.commit()
        return redirect(url_for('admin'))

@app.route('/listUser')
def listUser():
    # try:
    #     if current_user.email == 'admin@gmail.com':
    #         users = User.query.all()
    #         for i in users:
    #             if i.email == 'admin@gmail.com':
    #                 users.remove(i)
    return render_template('admin/usersList.html', users = users)

## Admin E-commerce Section Routes ##
@app.route('/productList')
def productList():
    data = refresh()
    return render_template('admin/productList.html', data = data)

@app.route('/adminViewproduct', methods=['GET', 'POST'])
def viewProduct():
    id = request.args.get('id')
    with open('json_files/product.json', 'r') as f:
        data = json.load(f)
        for i in data: 
            if i['id'] ==  int(id):
                product = i 
                break 
    review = Review.query.filter_by(prod_name=product['prod_name'])
    if str(review).find('SELECT') != None:
        review = None
    num = 0 if review == None else len(review) 
    with open('json_files/analytics.json', 'r') as f:
        data = json.load(f)
        for i in data: 
            if i['id'] ==  int(id):
                analytics = i 
                break 
    return render_template('admin/productDetail.html', product= product, review = review, analytics = analytics, num=num)

@app.route('/adminAddproduct', methods=['GET', 'POST'])
def adminAdd():
    form = AdminAddProductForm()
    if request.method == "POST":
        image = request.files['image']
        filename = request.files['image'].filename
        print(filename)
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
        print("Image saved")
        new_product_name = form.name.data
        new_product_price = form.price.data
        new_product_description = form.description.data
        new_product_id = form.id.data
        new_product_img = f"../static/product_img/{filename}"
        with open('json_files/product.json', 'r') as f:
            data = json.load(f)
            data.append({"id": int(new_product_id), "prod_name": new_product_name, "prod_price": new_product_price, "prod_desc": new_product_description, "prod_img": new_product_img})
        with open('json_files/product.json', 'w') as f:
            json.dump(data, f)
        return redirect(url_for('admin'))
    else:
        with open('json_files/product.json', 'r') as f: 
            data = json.load(f)
            latest_id = len(data)
    return render_template('admin/adminAddProduct.html', latest_id = latest_id+1, form=form)

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
        if filename:
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
        imagesrc = f'../static/img/profile_pic/{filename}'
        with open('json_files/product.json', 'r') as f:
            data = json.load(f)
            for i in data:
                if i["id"] == int(item_id):
                    i['prod_img'] = imagesrc
                    i['prod_name'] = item_name
                    i['prod_price'] = int(item_price)
                    i['prod_desc'] = item_desc
                    break
        with open('json_files/product.json', 'w') as f:
            json.dump(data, f)
        return redirect(url_for('admin'))
    elif productId != None:
        with open('json_files/product.json') as f:
            data = json.load(f)
            for i in data: 
                if i["id"] == int(productId):
                    product = i
                    break
            f.close()
        return render_template('admin/adminUpdateProduct.html', product = product, form=form)
    else:
        with open('json_files/product.json') as f:
            data = json.load(f)
            for i in data: 
                if i["id"] == 1:
                    product = i
                    break
        return render_template('admin/adminUpdateProduct.html', product = product, form=form)

@app.route('/addStock', methods=['POST', 'GET'])
def stock():
    if request.method == 'GET':
        id = request.args.get('id')
        data = refresh()
        for i in data: 
            if i['id'] == int(id):
                current = i
                break
        return render_template('admin/adminStock.html', data = current)
    else:
        with open('json_files/product.json', 'r') as f:
                data = json.load(f)
                productId = request.args.get('id')
                cun = request.form['quant[1]']
                for i in data: 
                    if i["id"] == int(productId):
                        i['stock'] += int(cun)
                        break
        with open('json_files/product.json', 'w') as f:
            json.dump(data, f)

        with open('json_files/analytics.json', 'r') as f:
                data = json.load(f)
                productId = request.args.get('id')
                cun = request.form['quant[1]']
                for i in data: 
                    if i["id"] == int(productId):
                        i['stock'] += int(cun)
                        break
        with open('json_files/analytics.json', 'w') as f:
            json.dump(data, f)
        return redirect(url_for('admin'))

"""Reset Password token routes"""

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='testemailnyp@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
   
@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    form = RequestResetForm()
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    form = ResetPasswordForm()
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

