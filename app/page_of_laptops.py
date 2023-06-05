from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products, Laptops


@app.route('/laptops')
def all_laptops():
    laptops = Products.query.filter_by(product_type='Laptop')
    return render_template('laptops.html', laptops=laptops)
