from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products, Laptops, Pcs, Phones, Tablet, Mouse, Keyboard

quantity = 0
p_id = 0
p_price = 0


@app.route('/product_Laptop/<int:product_id>')
def show_laptop(product_id):
    global quantity, p_id, p_price
    product = Products.query.filter_by(product_id=product_id).first()
    laptop_specs = Laptops.query.filter_by(foreign_key=product.product_id).first()
    p_price = product.product_price * quantity
    p_id = product.product_id
    return render_template('product_laptop.html',
                           product=product,
                           laptop_specs=laptop_specs,
                           quantity=quantity,
                           p_price=p_price)


@app.route('/product_PC/<int:product_id>')
def show_pc(product_id):
    global quantity, p_id, p_price
    product = Products.query.filter_by(product_id=product_id).first()
    pc_specs = Pcs.query.filter_by(foreign_key=product.product_id).first()
    p_price = product.product_price * quantity
    p_id = product.product_id
    return render_template('product_pc.html',
                           product=product,
                           pc_specs=pc_specs,
                           quantity=quantity,
                           p_price=p_price)


@app.route('/product_Phone/<int:product_id>')
def show_phone(product_id):
    global quantity, p_id, p_price
    product = Products.query.filter_by(product_id=product_id).first()
    phone_specs = Phones.query.filter_by(foreign_key=product.product_id).first()
    p_price = product.product_price * quantity
    p_id = product.product_id
    return render_template('product_phone.html',
                           product=product,
                           phone_specs=phone_specs,
                           quantity=quantity,
                           p_price=p_price)


@app.route('/product_Tablet/<int:product_id>')
def show_tablet(product_id):
    global quantity, p_id, p_price
    product = Products.query.filter_by(product_id=product_id).first()
    tablet_specs = Tablet.query.filter_by(foreign_key=product.product_id).first()
    p_price = product.product_price * quantity
    p_id = product.product_id
    return render_template('product_tablet.html',
                           product=product,
                           tablet_specs=tablet_specs,
                           quantity=quantity,
                           p_price=p_price)


@app.route('/product_Mouse/<int:product_id>')
def show_mouse(product_id):
    global quantity, p_id, p_price
    product = Products.query.filter_by(product_id=product_id).first()
    mouse_specs = Mouse.query.filter_by(foreign_key=product.product_id).first()
    p_price = product.product_price * quantity
    p_id = product.product_id
    return render_template('product_mouse.html',
                           product=product,
                           mouse_specs=mouse_specs,
                           quantity=quantity,
                           p_price=p_price)


@app.route('/product_Keyboard/<int:product_id>')
def show_keyboard(product_id):
    global quantity, p_id, p_price
    product = Products.query.filter_by(product_id=product_id).first()
    keyboard_specs = Keyboard.query.filter_by(foreign_key=product.product_id).first()
    p_price = product.product_price * quantity
    p_id = product.product_id
    return render_template('product_keyboard.html',
                           product=product,
                           keyboard_specs=keyboard_specs,
                           quantity=quantity,
                           p_price=p_price)


@app.route('/add_quantity/<product_type>')
def add_q(product_type):
    global quantity
    quantity += 1
    return redirect(f'/product_{product_type}/{p_id}')


@app.route('/remove_quantity/<product_type>')
def remove_q(product_type):
    global quantity
    quantity -= 1
    return redirect(f'/product_{product_type}/{p_id}')

