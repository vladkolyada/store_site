from .loader import app
from flask import render_template, flash, redirect, url_for
from .data_base import Products, Laptops


@app.route('/')
def home():
    return render_template('base.html', title='Магазин комп.тех. (HOME)')


<<<<<<< HEAD
@app.route('/laptops/brand/<brand>')
def filters(brand):
    laptop_brand = Laptops.quary.filter_by(orand=filter)
    product = Products.quary.filter_by(id=laptop.faregin_key)



=======
@app.route('/laptops/brand/<filter>')
def laptop_filter(filter):
    laptop = Laptops.query.filter_by(brand=filter)
    product = Products.query.filter_by(id=laptop.foreign_key)
    render_template('laptops.html', product=product)

    
>>>>>>> 1c34a14f9fc33bf37f8afcdba526220c62501b41


