from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LogInAdmin(FlaskForm):
    password=PasswordField('password',validators =[DataRequired()])
    username=StringField('name',validators =[DataRequired()])
    remember_me = BooleanField('Remember?')
    submit = SubmitField('Enter')

class LoginUser(FlaskForm):
    password=PasswordField('password',validators =[DataRequired()])
    username=StringField('name',validators =[DataRequired()])
    email=StringField('Email', validators=[DataRequired(), Email()])
    remember_me = BooleanField('Remember?')
    submit = SubmitField('Enter')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
