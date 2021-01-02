import os, logging
from flask import Flask
from authlib.integrations.flask_client import OAuth
# from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from logging.config import dictConfig
from datetime import timedelta
from flask.logging import default_handler
from flask import Flask, session
# from flask_session import Session
from datetime import timedelta

#sqlite database setup and configurations
app = Flask(__name__)
app.logger.removeHandler(default_handler)
app.config['SECRET_KEY'] = '1250886c25d8cdc3533957d2f96a4b03'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=60)
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# images
app.config['IMAGE_UPLOADS'] = 'controllers\static\product_img'
app.config['PROFILE_UPLOADS'] = 'controllers\static\img\profile_pic'
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ['JPEG', 'PNG', 'JPG', 'GIF']
# db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
key = b'Yf7wsTW0knSSY03n3IGF1_QmhvvZCYYqrkBXGlh0Hng='

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id="381762809201-8lek8fp7d5o34n96dcv5svn7419m92en.apps.googleusercontent.com",
    client_secret="I9rEV6dUWq-YirIbGJ10zBLK",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)


#login system configurations
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'

#smtp email configurations
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'testemailnyp@gmail.com'
app.config['MAIL_PASSWORD'] = 'ValentiaTest2@@1'
mail = Mail(app)

from controllers import routes
