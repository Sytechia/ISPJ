"""
User model
"""
from datetime import datetime, timedelta
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from controllers import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.String(20), nullable=False, default='Active')
    fullname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='../static/img/profile_pic/default.jpg')
    password = db.Column(db.String(60), nullable=False)
    products = db.relationship('Product', backref='author', lazy=True)
    isAdmin = db.Column(db.String(60), nullable=False)
    review = db.relationship('ProductReview', backref='author', lazy=True)
    address_info = db.relationship('AddressInfo', backref='author', lazy=True)
    card_info = db.relationship('CardInfo', backref='author', lazy=True)
    previousTransactions = db.relationship('PreviousTransactions', backref='author', lazy=True)
    previousPasswords = db.Column(db.Text, nullable=True)

    def get_reset_token(self, expires_sec=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.fullname}', '{self.email}', '{self.image_file}')"


    


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod_quantity = db.Column(db.Integer, nullable=False)
    prod_name = db.Column(db.String(100), nullable=False)
    prod_price = db.Column(db.Integer, nullable=False)
    prod_desc = db.Column(db.Text, nullable=False)
    img = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Product('{self.prod_name}', '{self.prod_quantity}', '{self.prod_price}', '{self.img}')"


class AddressInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100),nullable=False)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    postal = db.Column(db.Integer, nullable=False)
    default = db.Column(db.String(20), nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Address-Info('{self.address}', '{self.country}', '{self.state}', '{self.postal}' '{self.user_id}')"


class CardInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(100), nullable=False)
    cardno = db.Column(db.Text, unique=True)
    exp = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(100), nullable=False)
    default = db.Column(db.String(20), nullable=False, default=False)
    card_type = db.Column(db.String(20), nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(100), nullable=False)
    prod_name = db.Column(db.String(100), nullable=False)
    prod_quantity = db.Column(db.Integer, nullable=False)
    prod_price = db.Column(db.Integer, nullable=False)
    prod_desc = db.Column(db.Text, nullable=False)
    date_purchase = db.Column(db.DateTime, nullable=False, default=(datetime.utcnow()+timedelta(hours=8, minutes=8)))
    img = db.Column(db.String(60), nullable=False)
    transaction_id = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class ProductReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod_id = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(1000), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class PreviousTransactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cartItems = db.Column(db.String(1000), nullable=False)
    transactionId = db.Column(db.String(100), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False, default=(datetime.utcnow()+timedelta(hours=8, minutes=8)))
    status = db.Column(db.String(50), nullable=False, default='Awaiting order')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)




