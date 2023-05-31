from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products, Laptops

basket = []


@app.route('/buy/<product_name>')
def add_to_basket(product_name):
    global basket
    basket.append(product_name)
    return redirect('/product/<product_name>')


@app.route('/basket')
def show_basket():
    global basket
    return render_template('basket.html', basket=basket)


@app.route("/delete/<product>")
def remove_product_from_basket(product):
    global basket
    basket.remove(product)
    return redirect('/basket')



