from .loader import app
from flask import render_template, flash, redirect, url_for
from .data_base import Products, Laptops, Pcs, Phones, Tablet, Mouse, Keyboard


@app.route('/')
def home():
    all_products = Products.query.all()
    return render_template('base.html', title='Магазин комп.тех. (HOME)', all_products=all_products)


@app.route('/laptops/color/<color>')
def color_filter_laptops(color):
    laptops = []
    laptop_filter = Laptops.query.filter_by(color=color)
    for i in laptop_filter:
        laptops.append(Products.query.filter_by(product_id=i.foreign_key).first())
    return render_template('laptops.html', laptops=laptops)


@app.route('/laptops/brand/<brand>')
def brand_filter_laptops(brand):
    laptops = []
    laptop_filter = Laptops.query.filter_by(brand=brand)
    for i in laptop_filter:
        laptops.append(Products.query.filter_by(product_id=i.foreign_key).first())
    return render_template('laptops.html', laptops=laptops)


@app.route('/pcs/color/<color>')
def color_filter_pcs(color):
    pcs = []
    pcs_filter = Pcs.query.filter_by(color=color)
    for pc in pcs_filter:
        pcs.append(Products.query.filter_by(product_id=pc.foreign_key).first())
    return render_template('pcs.html', pcs=pcs)


@app.route('/phones/color/<color>')
def color_filter_phones(color):
    phones = []
    phones_filter = Phones.query.filter_by(color=color)
    for phone in phones_filter:
        phones.append(Products.query.filter_by(product_id=phone.foreign_key).first())
    return render_template('phones.html', phones=phones)


@app.route('/phones/brand/<brand>')
def brand_filter_phones(brand):
    phones = []
    phones_filter = Phones.query.filter_by(brand=brand)
    for phone in phones_filter:
        phones.append(Products.query.filter_by(product_id=phone.foreign_key).first())
    return render_template('phones.html', phones=phones)


@app.route('/tablets/color/<color>')
def color_filter_tablets(color):
    tablets = []
    tablets_filter = Tablet.query.filter_by(color=color)
    for tablet in tablets_filter:
        tablets.append(Products.query.filter_by(product_id=tablet.foreign_key).first())
    return render_template('tablets.html', tablets=tablets)


@app.route('/tablets/brand/<brand>')
def brand_filter_tablets(brand):
    tablets = []
    tablets_filter = Tablet.query.filter_by(brand=brand)
    for tablet in tablets_filter:
        tablets.append(Products.query.filter_by(product_id=tablet.foreign_key).first())
    return render_template('tablets.html', tablets=tablets)


@app.route('/mice/color/<color>')
def color_filter_mice(color):
    mice = []
    mice_filter = Mouse.query.filter_by(color=color)
    for mouse in mice_filter:
        mice.append(Products.query.filter_by(product_id=mouse.foreign_key).first())
    return render_template('mice.html', mice=mice)


@app.route('/mice/brand/<brand>')
def brand_filter_mice(brand):
    mice = []
    mice_filter = Mouse.query.filter_by(brand=brand)
    for mouse in mice_filter:
        mice.append(Products.query.filter_by(product_id=mouse.foreign_key).first())
    return render_template('mice.html', mice=mice)


@app.route('/keyboards/color/<color>')
def color_filter_keyboards(color):
    keyboards = []
    keyboards_filter = Keyboard.query.filter_by(color=color)
    for keyboard in keyboards_filter:
        keyboards.append(Products.query.filter_by(product_id=keyboard.foreign_key).first())
    return render_template('keyboards.html', keyboards=keyboards)


@app.route('/keyboards/brand/<brand>')
def brand_filter_keyboards(brand):
    keyboards = []
    keyboards_filter = Keyboard.query.filter_by(brand=brand)
    for keyboard in keyboards_filter:
        keyboards.append(Products.query.filter_by(product_id=keyboard.foreign_key).first())
    return render_template('keyboards.html', keyboards=keyboards)


