from flask import Flask, render_template, redirect, url_for, flash

from . import forms
from .forms import LogInAdmin, RegistrationForm, LoginUser
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.data_base import AdminUsers, Users, db
from app.loader import app

login = LoginManager(app)
login.login_view = "login"


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


@login.user_loader
def load_user(id):
    return AdminUsers.query.get(int(id))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_name = form.username.data
        email = form.email.data
        password = form.password.data
        user = Users(user_name=user_name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('sign_up.html', form=form)


@app.route('/log_in', methods=['GET','POST'])
def log_in():
    form = LoginUser()
    if current_user.is_authenticated:
        return redirect('/')
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/log_in')
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('log_in.html', form=form)


@login_required
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
