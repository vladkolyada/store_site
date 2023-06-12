from .loader import app
from flask import render_template, flash, redirect, url_for
from .data_base import Products, Laptops


@app.route('/')
def home():
    all_products = Products.query.all()
    return render_template('base.html', title='Магазин комп.тех. (HOME)', all_products=all_products)


@app.route('/laptops/color/<color>')
def color_filter(color):
    laptops = []
    laptop_filter = Laptops.query.filter_by(color=color)
    for i in laptop_filter:
        laptops.append(Products.query.filter_by(product_id=i.foreign_key).first())
    return render_template('laptops.html', laptops=laptops)


@app.route('/laptops/brand/<brand>')
def brand_filter(brand):
    laptops = []
    laptop_filter = Laptops.query.filter_by(brand=brand)
    for i in laptop_filter:
        laptops.append(Products.query.filter_by(product_id=i.foreign_key).first())
    return render_template('laptops.html', laptops=laptops)


