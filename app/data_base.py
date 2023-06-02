from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin

from app.loader import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Admin(UserMixin, db.Model):
    password = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)


class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_image_name = db.Column(db.String(10), unique=True)
    product_type = db.Column(db.String(20))
    # тут повинні бути, тільки такі слова як: Laptop, PC, Phone, Tablet, Keyboard, Mouse, Headphones. Більше ніякі!
    product_title = db.Column(db.String(150), unique=True)
    product_price = db.Column(db.Integer, nullable=False)


class Laptops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foreign_key = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    processor_specifications = db.Column(db.String(150))
    memory_capacity_specifications = db.Column(db.String(250))
    display_characteristics = db.Column(db.String(200))
    ram_specifications = db.Column(db.String(200))
    number_of_ram_slots = db.Column(db.Integer)
    graphics_card_specifications = db.Column(db.String(250))
