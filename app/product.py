from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products, Laptops

quantity = 0
p_id = 0
p_price = 0


@app.route('/product/<int:product_id>')
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


@app.route('/add_quantity')
def add_q():
    global quantity
    quantity += 1
    return redirect(f'/product/{p_id}')


@app.route('/remove_quantity')
def remove_q():
    global quantity
    quantity -= 1
    return redirect(f'/product/{p_id}')

