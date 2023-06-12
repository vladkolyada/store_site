from .loader import app
from flask import render_template, flash, redirect, url_for
from .data_base import Products, Laptops


@app.route('/')
def home():
    all_products = Products.query.all()
    return render_template('base.html', title='Магазин комп.тех. (HOME)', all_products=all_products)





