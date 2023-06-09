from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products


@app.route('/laptops')
def all_laptops():
    laptops = Products.query.filter_by(product_type='Laptop')
    return render_template('laptops.html', laptops=laptops)


@app.route('/pcs')
def all_pcs():
    pcs = Products.query.filter_by(product_type='PC')
    return render_template('pcs.html', pcs=pcs)


@app.route('/phones')
def all_phones():
    phones = Products.query.filter_by(product_type='Phone')
    return render_template('Phones.html', phones=phones)


@app.route('/tablets')
def all_tablets():
    tablets = Products.query.filter_by(product_type='Tablet')
    return render_template('tablets.html', tablets=tablets)


@app.route('/mice')
def all_mice():
    mice = Products.query.filter_by(product_type='Mouse')
    return render_template('mice.html', mice=mice)


@app.route('/keyboards')
def all_keyboards():
    keyboards = Products.query.filter_by(product_type='Keyboard')
    return render_template('keyboards.html', keyboards=keyboards)
