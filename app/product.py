from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products


@app.route('/product/<product_image_name>')
def show_product(product_image_name):
    product = Products.query.filter_by(product_image_name=str(327632806)).first()
    return render_template('product.html', product=product)
