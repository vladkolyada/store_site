from flask import Flask, render_template,redirect,url_for

from . import forms
from .forms import LogInAdmin,RegistrationForm,LoginUser

from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from app.data_base import AdminUsers, Users
from app.loader import app


@app.route('/sign_up')
def signup():
    form = RegistrationForm()
    return render_template('sign_up.html', form=form)

@app.route('/log_in')
def log_in():
    form = LoginUser()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('log'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('log_in.html', form=form)


@app.route('/log_in_for_admins', methods=['GET', 'POST'])
def log_in_admin():
    form = LogInAdmin()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = AdminUsers.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return redirect('/log_in')
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('registeradmin.html', title='Увійти', form=form)
