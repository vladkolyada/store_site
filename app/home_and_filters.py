from .loader import app
from flask import render_template, flash, redirect, url_for


@app.route('/')
def hi():
    return render_template('base.html')
