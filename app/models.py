from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

# create Models based off of our ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    cart = db.relationship('Cart', backref='Owner', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    image = db.Column(db.String)
    price = db.Column(db.Integer)
    qty = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __init__(self, title, image, price, qty, user_id):
        self.title = title
        self.image = image
        self.price = price
        self.qty = qty
        self.user_id = user_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()