from .loader import app
from flask import render_template, flash, redirect, url_for
from .data_base import Products, Laptops


@app.route('/')
def home():
    return render_template('base.html', title='Магазин комп.тех. (HOME)')


@app.route('/laptops/brand/<brand>')
def filters(brand):
    laptop_brand = Laptops.quary.filter_by(orand=filter)
    product = Products.quary.filter_by(id=laptop.faregin_key)





