from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin

from app.loader import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_image_name = db.Column(db.String(10), unique=True)
    product_title = db.Column(db.String(150), unique=True)
    product_price = db.Column(db.Integer, nullable=False)


class Laptops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foreign_key = db.Column(db.Integer, db.ForeignKey('products.product_id'))
