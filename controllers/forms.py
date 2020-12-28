"""
Validators + form model 
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import *
from wtforms.validators import *
from controllers.models import User
from flask_login import current_user
import re, base64
from password_strength import PasswordPolicy
from datetime import datetime


class RegistrationForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

countries = [('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua & Deps', 'Antigua & Deps'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia Herzegovina', 'Bosnia Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina', 'Burkina'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), ('Central African Rep', 'Central African Rep'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Congo {Democratic Rep}', 'Congo {Democratic Rep}'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland {Republic}', 'Ireland {Republic}'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Ivory Coast', 'Ivory Coast'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea North', 'Korea North'), ('Korea South', 'Korea South'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Micronesia', 'Micronesia'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar, {Burma}', 'Myanmar, {Burma}'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('St Kitts & Nevis', 'St Kitts & Nevis'), ('St Lucia', 'St Lucia'), ('Saint Vincent & the Grenadines', 'Saint Vincent & the Grenadines'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Sao Tome & Principe', 'Sao Tome & Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatican City', 'Vatican City'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')]
class Billing(FlaskForm):
    address = StringField('Address', validators=[DataRequired(), Length(min=8, max=100)])
    # country = StringField('country', validators=[DataRequired(), Length(min=2, max=20)])
    # def validate_country(form, field):
    #     pattern = '^[a-zA-Z\s]*$'
    #     result = re.match(pattern, field.data)
    #     if not result:
    #         raise ValidationError("Invalid country name")
    country = SelectField('Country', choices=countries)
    state = StringField('state', validators=[DataRequired(), Length(min=2, max=20)])
    def validate_state(form, field):
        pattern = '^[a-zA-Z\s]*$'
        result = re.match(pattern, field.data)
        print(result)
        if not result:
            raise ValidationError("Invalid state name")
    postal = StringField('postal', validators=[DataRequired(), Length(min=6, max=6)])
    def validate_postal(form, field):
        pattern = '^[0-9]*$'
        result = re.match(pattern, field.data)
        if not result:
            raise ValidationError("Invalid postal code")
    submit = SubmitField('Submit')


class PaymentInfo(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    def validate_name(form, field):
        pattern = '^[a-zA-Z\s]*$'
        result = re.match(pattern, field.data)
        if not result:
            raise ValidationError("Invalid card name")
    cardno = StringField('Fullname', validators=[DataRequired(), Length(min=16, max=16)])

    def validate_cardno(form, field):

        def sum_digits(digit):
            if digit < 10:
                return digit
            else:
                sum = (digit % 10) + (digit // 10)
                return sum

        def validate(cc_num):
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
            return sum_of_digits % 10 == 0

        if field.data[0] not in ['4', '5']:
            raise ValidationError("Invalid card number")
        elif(validate(field.data) == False):
            raise ValidationError("Invalid card number")
        else:
            return True
        
    exp = StringField('Month', validators=[DataRequired(), Length(min=1, max=2)])
    def validate_exp(form, field):
        current_month = int(datetime.now().month)
        months = [str(i) for i in range(current_month, 13)]
        if field.data not in months:
            raise ValidationError('Invalid expiry month!')
        else:
            return True
    year = StringField('Year', validators=[DataRequired(), Length(min=4, max=4)])
    def validate_year(form, field):
        year_accepted = ["2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028"]
        if field.data not in year_accepted:
            raise ValidationError('Invalid expiry year!')    
        else:
            return True
    submit = SubmitField('Submit')


class Disable(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Disable')

class ReviewForm(FlaskForm):
    comments = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Activate(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Activate')

class UpdateCard(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    def validate_name(form, field):
        pattern = '^[a-zA-Z\s]*$'
        result = re.match(pattern, field.data)
        if not result:
            raise ValidationError("Invalid card name")
    
    cardno = StringField('Fullname', validators=[DataRequired(), Length(min=16, max=16)])
    def validate_cardno(form, field):
        def sum_digits(digit):
            if digit < 10:
                return digit
            else:
                sum = (digit % 10) + (digit // 10)
                return sum


        def validate(cc_num):
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
            return sum_of_digits % 10 == 0
        
        if field.data[0] not in ['4', '5']:
            raise ValidationError("Invalid card number")
        elif(validate(field.data) == False):
            raise ValidationError("Invalid card number")
        else:
            return True

    exp = StringField('Month', validators=[DataRequired(), Length(min=1, max=2)])
    def validate_exp(form, field):
        current_month = int(datetime.now().month)
        months = [str(i) for i in range(current_month, 13)]
        if field.data not in months:
            raise ValidationError('Invalid expiry month!')
        else:
            return True
    year = StringField('Fullname', validators=[DataRequired(), Length(min=4, max=4)])
    def validate_year(form, field):
        year_accepted = ["2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028"]
        if field.data not in year_accepted:
            raise ValidationError('Invalid expiry year!')    
        else:
            return True
    submit = SubmitField('Submit')


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), Length(min=8, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Change')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    

class UpdateAccountForm(FlaskForm):
    fullname = StringField('Fullname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class UpdateBilling(FlaskForm):
    address = StringField('Address', validators=[DataRequired(), Length(min=8, max=100)])
    country = SelectField('Country', choices=countries)
    state = StringField('Address', validators=[DataRequired(), Length(min=2, max=20)])
    def validate_state(form, field):
        print(field.data)
        pattern = '^[a-zA-Z\s]*$'
        result = re.match(pattern, field.data)
        print(result)
        if result == None:
            raise ValidationError("Invalid state name")
    postal = StringField('Address', validators=[DataRequired(), Length(min=6, max=6)])
    def validate_postal(form, field):
        pattern = '^[0-9]*$'
        result = re.match(pattern, field.data)
        if not result:
            raise ValidationError("Invalid postal code")
    submit = SubmitField('Submit')


class PasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Change Password')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            pass
        else:
            raise ValidationError('Invalid email. Please try again!')




class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset')

class ContactUs(FlaskForm):
    fullname = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    radio = RadioField('Contact type', choices=[('enquiry','Enquiry'),('feedback','Feedback')])
    feedback = TextAreaField('Feedback', [DataRequired()])
    submit = SubmitField('Submit')

class AdminUpdateProductForm(FlaskForm):
    id = StringField('id')
    
    name = StringField('Item Name', validators=[data_required(), Length(min=5, max=30)])

    description = StringField('Item desciption', validators=[data_required(), Length(min=5, max=30)])

    price = StringField('Item Price', validators=[data_required(), Length(min=5, max=30)])

    stock = StringField('Stock', validators=[data_required(), Length(min=5, max=30)])

    submit = SubmitField('Submit')

class AdminAddProductForm(FlaskForm):
    id = StringField('id')

    name = StringField('Item Name', validators=[data_required(), Length(min=5, max=30)])

    img = FileField('Image Source', validators=[FileRequired()])

    description = StringField('Item desciption', validators=[data_required(), Length(min=5, max=30)])

    price = StringField('Item Price', validators=[data_required(), Length(min=5, max=30)])

    submit = SubmitField('Add Item')


 