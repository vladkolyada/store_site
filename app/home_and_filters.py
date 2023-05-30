from .loader import app
from flask import render_template, flash, redirect, url_for


@app.route('/')
def home():
    return render_template('base.html', title='Магазин комп.тех. (HOME)')
