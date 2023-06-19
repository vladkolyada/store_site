from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LogInAdmin(FlaskForm):
    password = PasswordField('password',validators =[DataRequired()])
    username = StringField('name',validators =[DataRequired()])
    remember_me = BooleanField('Remember?')
    submit = SubmitField('Enter')


class AddProduct(FlaskForm):
    product_image_name = StringField('Імя_зображення_продукту',validators =[DataRequired()])
    product_type = StringField('Тип_продукту',validators =[DataRequired()])
    product_title = StringField('Назва_продукту',validators =[DataRequired()])
    product_description = StringField('Опис_продукту',validators =[DataRequired()])
    product_price = StringField('Ціна_товару',validators =[DataRequired()])
    submit = SubmitField('Enter')


class LoginUser(FlaskForm):
    password = PasswordField('password',validators =[DataRequired()])
    username = StringField('name',validators =[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    remember_me = BooleanField('Remember?')
    submit = SubmitField('Enter')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class characterleptop(FlaskForm):
    color = StringField('Колір', validators=[DataRequired(), Email()])
    brand = StringField('Бренд', validators=[DataRequired(), Email()])
    processor_specifications = StringField('Характеристики процесора', validators=[DataRequired(), Email()])
    graphics_card_specifications = StringField('Характеристики обєма памяті', validators=[DataRequired(), Email()])
    ram_specifications = StringField('Характеристики дисплея', validators=[DataRequired(), Email()])
    memory_capacity_specifications = StringField('Характеристики оперативної памяті', validators=[DataRequired(), Email()])
    display_characteristics = StringField('Характеристики відеокарти', validators=[DataRequired(), Email()])
class characterPc(FlaskForm):
    color =StringField('Колір', validators=[DataRequired(), Email()])
    processor_specifications =StringField('Характеристики процесора', validators=[DataRequired(), Email()])
    graphics_card_specifications = StringField('Характеристики відеокарти', validators=[DataRequired(), Email()])
    ram_specifications = StringField('Характеристики обєма памяті', validators=[DataRequired(), Email()])
    number_of_ram_slots = StringField('Характеристики оперативної памяті', validators=[DataRequired(), Email()])
    specifications_motherboard = StringField('Кількість слотів оперативної памяті', validators=[DataRequired(), Email()])
    memory_capacity_specifications = StringField('Характеристики материнської плати', validators=[DataRequired(), Email()])
    cpu_cooling = StringField('Характеристики охолодження', validators=[DataRequired(), Email()])
    power_supply_specifications = StringField('Характеристики блока живлення', validators=[DataRequired(), Email()])
    case_characteristics = StringField('Характеристики корпуса', validators=[DataRequired(), Email()])