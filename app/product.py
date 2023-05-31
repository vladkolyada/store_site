from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products, Laptops


@app.route('/product/<product_image_name>')
def show_product(product_image_name):
    product = Products.query.filter_by(product_image_name=str(327632806)).first()
    product_specs = Laptops.query.filter_by(foreign_key=product.product_id).first()
    return render_template('product.html', product=product, product_specs=product_specs)
