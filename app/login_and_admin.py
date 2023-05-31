from flask import Flask, render_template,redirect,url_for
from .forms import LogIn,RegistrationForm

from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from app.data_base import Admin
from app.loader import app


@app.route('/signup')
def signup():
    form=RegistrationForm()
    return render_template('sign up.html', form=form)


@app.route('/login1', methods=['GET', 'POST'])
def log_in1():
    form = LogIn()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Admin.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return redirect('/login1')
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('registeradmin.html', title='Увійти', form=form)
