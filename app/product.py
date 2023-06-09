from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products, Laptops


@app.route('/product/<product_title>')
def show_product(product_title):
    product = Products.query.filter_by(product_title=product_title).first()
    product_specs = Laptops.query.filter_by(foreign_key=product.product_id).first()
    return render_template('product.html', product=product, product_specs=product_specs)
