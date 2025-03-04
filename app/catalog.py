from .loader import app
from flask import render_template, flash, redirect, url_for


@app.route('/catalog')
def catalog_of_products():
    return render_template('catalog.html')
