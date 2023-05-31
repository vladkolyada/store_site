from app.loader import app
from flask import render_template, flash, redirect, url_for
from .data_base import *
from app.data_base import Products, Laptops


basket = []


@app.route('/basket/<c>')
def basket(c):
    global basket
    return render_template('basket.html', basket=basket)
