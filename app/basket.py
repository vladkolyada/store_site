
from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products, Laptops

basket = []
name_p = ""


@app.route('/buy/<product_name>')
def add_to_basket(product_name):
    global basket, name_p
    basket.append(product_name)
    name_p = f"{product_name}"
    return redirect(f'/product/{product_name}')


@app.route('/basket')
def show_basket():
    global basket, name_p
    price = Products.query.filter_by(product_title=name_p).first()
    return render_template('basket.html', basket=basket, price=price)


@app.route("/delete/<product>")
def remove_product_from_basket(product):
    global basket
    basket.remove(product)
    return redirect('/basket')




