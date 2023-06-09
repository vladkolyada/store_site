from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products, Laptops


@app.route('/product/<int:product_id>')
def show_laptop(product_id):
    product = Products.query.filter_by(product_id=product_id).first()
    laptop_specs = Laptops.query.filter_by(foreign_key=product.product_id).first()
    print(laptop_specs)
    return render_template('product.html', product=product, laptop_specs=laptop_specs)
