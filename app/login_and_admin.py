from flask import render_template, redirect, url_for, flash, request
from .forms import LogInAdmin, RegistrationForm, LoginUser, AddProduct
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.data_base import AdminUsers, Users, db
from app.loader import app

login = LoginManager(app)
login.login_view = "log_in"


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


@login.user_loader
def load_user(id):
    return AdminUsers.query.get(int(id))


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


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


@login_required
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProduct()
    product_type = request.form.get('product_type')
    product_image_name = request.form.get('product_image_name')
    product_title = request.form.get('product_title')
    product_description = request.form.get('product_description')
    product_price = request.form.get('product_price')

    if product_type == "laptop":
        return redirect(
            url_for('laptop', image_name=product_image_name, title=product_title, description=product_description,
                    price=product_price))
    elif product_type == "PC":
        return redirect(
            url_for('PC', image_name=product_image_name, title=product_title, description=product_description,
                    price=product_price))
    elif product_type == "Phone":
        return redirect(
            url_for('Phone', image_name=product_image_name, title=product_title, description=product_description,
                    price=product_price))
    elif product_type == "Tablet":
        return redirect(
            url_for('Tablet', image_name=product_image_name, title=product_title, description=product_description,
                    price=product_price))
    elif product_type == "Mouse":
        return redirect(
            url_for('Mouse', image_name=product_image_name, title=product_title, description=product_description,
                    price=product_price))
    elif product_type == "Headphones":
        return redirect(
            url_for('Headphones', image_name=product_image_name, title=product_title, description=product_description,
                    price=product_price))
    return render_template('addproduct.html', form=form)


@app.route('/laptop')
def laptop():
    image_name = request.args.get('image_name')
    title = request.args.get('title')
    description = request.args.get('description')
    price = request.args.get('price')
    return render_template('laptop.html', image_name=image_name, title=title, description=description, price=price)


@app.route('/PC', methods=['GET', 'POST'])
def pc():
    image_name = request.args.get('image_name')
    title = request.args.get('title')
    description = request.args.get('description')
    price = request.args.get('price')
    return render_template('pc.html', image_name=image_name, title=title, description=description, price=price)


@app.route('/Phone', methods=['GET', 'POST'])
def phone():
    image_name = request.args.get('image_name')
    title = request.args.get('title')
    description = request.args.get('description')
    price = request.args.get('price')
    return render_template('phone.html', image_name=image_name, title=title, description=description, price=price)


@app.route('/Tablet', methods=['GET', 'POST'])
def tablet():
    image_name = request.args.get('image_name')
    title = request.args.get('title')
    description = request.args.get('description')
    price = request.args.get('price')
    return render_template('tablet.html', image_name=image_name, title=title, description=description, price=price)


@app.route('/Keyboard', methods=['GET', 'POST'])
def keyboard():
    image_name = request.args.get('image_name')
    title = request.args.get('title')
    description = request.args.get('description')
    price = request.args.get('price')
    return render_template('keyboard.html', image_name=image_name, title=title, description=description, price=price)


@app.route('/Mouse', methods=['GET', 'POST'])
def mouse():
    image_name = request.args.get('image_name')
    title = request.args.get('title')
    description = request.args.get('description')
    price = request.args.get('price')
    return render_template('mouse.html', image_name=image_name, title=title, description=description, price=price)


@app.route('/Headphones', methods=['GET', 'POST'])
def head_phones():
    image_name = request.args.get('image_name')
    title = request.args.get('title')
    description = request.args.get('description')
    price = request.args.get('price')
    return render_template('headphones.html', image_name=image_name, title=title, description=description, price=price)


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    form = LoginUser()
    if current_user.is_authenticated:
        return redirect('/')
    if form.validate_on_submit():
        user = Users.query.filter_by(user_name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/log_in')
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('log_in.html', form=form)


@app.route('/log_in_for_admins', methods=['GET', 'POST'])
def log_in_admin():
    form = LogInAdmin()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = AdminUsers.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return redirect('/log_in_for_admins')
        login_user(user, remember=form.remember_me.data)
        return redirect('/add_product')
    return render_template('registeradmin.html', title='Увійти', form=form)
