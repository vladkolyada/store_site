from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
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


class Otpavka(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    phone = StringField('number', validators=[DataRequired()])
    adressa = SelectField('adressa', choices=[('Kiev', 'Kiev'), ('chernivci', 'Chernivci')])
    dostavka = SelectField('sposib dostavki', choices=[('Ukrposhta', 'Ukrposhta'), ('olx', 'Olx')])
    send = SubmitField('Submit')

