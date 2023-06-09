from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.loader import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Users {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class AdminUsers(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), nullable=False, unique=True)
    password_hash = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<AdminUsers {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_image_name = db.Column(db.String(65), unique=True, index=True)
    product_type = db.Column(db.String(20), index=True)
    # тут повинні бути, тільки такі слова як: Laptop, PC, Phone, Tablet, Keyboard, Mouse, Headphones. Більше ніякі!
    product_title = db.Column(db.String(150), unique=True, index=True)
    product_description = db.Column(db.String(450), index=True)
    product_price = db.Column(db.Integer, nullable=False)


class Laptops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foreign_key = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    color = db.Column(db.String(30))
    brand = db.Column(db.String(50))
    processor_specifications = db.Column(db.String(150))
    graphics_card_specifications = db.Column(db.String(250))
    ram_specifications = db.Column(db.String(200))
    number_of_ram_slots = db.Column(db.Integer)
    memory_capacity_specifications = db.Column(db.String(250))
    display_characteristics = db.Column(db.String(200))
    producing_country = db.Column(db.String(50))


class Pcs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foreign_key = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    color = db.Column(db.String(30))
    processor_specifications = db.Column(db.String(150))
    graphics_card_specifications = db.Column(db.String(250))
    ram_specifications = db.Column(db.String(200))
    number_of_ram_slots = db.Column(db.Integer)
    specifications_motherboard = db.Column(db.String(200))
    memory_capacity_specifications = db.Column(db.String(250))
    cpu_cooling = db.Column(db.String(150))
    power_supply_specifications = db.Column(db.String(100))
    case_characteristics = db.Column(db.String(120))
    producing_country = db.Column(db.String(50))


class Phones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foreign_key = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    brand = db.Column(db.String(50))
    color = db.Column(db.String(30))
    communication_standard_or_internet = db.Column(db.String(150))
    display_characteristics = db.Column(db.String(200))
    SIM_card_characteristics = db.Column(db.String(100))
    characteristics_memory_functions = db.Column(db.String(150))
    operating_system = db.Column(db.String(60))
    characteristics_of_the_front_camera = db.Column(db.String(200))
    processor_specifications = db.Column(db.String(150))
    characteristics_of_the_main_camera = db.Column(db.String(200))
    power_characteristics = db.Column(db.String(100))
    connectors = db.Column(db.String(150))
    navigation = db.Column(db.String(80))
    dimensions = db.Column(db.String(200))
    producing_country = db.Column(db.String(50))


class Tablet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foreign_key = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    color = db.Column(db.String(30))
    brand = db.Column(db.String(50))
    display_characteristics = db.Column(db.String(200))
    characteristics_memory_functions = db.Column(db.String(150))
    operating_system = db.Column(db.String(60))
    characteristics_of_the_front_camera = db.Column(db.String(200))
    processor_specifications = db.Column(db.String(150))
    characteristics_of_the_main_camera = db.Column(db.String(200))
    power_characteristics = db.Column(db.String(100))
    connectors = db.Column(db.String(150))
    navigation = db.Column(db.String(80))
    dimensions = db.Column(db.String(200))
    producing_country = db.Column(db.String(50))


class Mouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foreign_key = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    connection = db.Column(db.String(50))
    size = db.Column(db.String(50))
    interface = db.Column(db.String(50))
    number_of_mouse_buttons = db.Column(db.Integer)
    color = db.Column(db.String(30))
    brand = db.Column(db.String(50))
    weight = db.Column(db.String(50))
    sensor_type = db.Column(db.String(60))
    additional_functions = db.Column(db.String(300))
    dimensions = db.Column(db.String(200))
    cable_length = db.Column(db.String(10))
    producing_country = db.Column(db.String(50))


class Keyboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foreign_key = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    number_of_keyboard_buttons = db.Column(db.Integer)
    producing_country = db.Column(db.String(50))
    backlight_color = db.Column(db.String(50))
    keyboard_layout = db.Column(db.String(100))
    interface = db.Column(db.String(100))
    weight = db.Column(db.String(20))
    appointment = db.Column(db.String(100))
    cable_length = db.Column(db.String(20))
    dimensions = db.Column(db.String(200))

