from app.loader import app
from flask import render_template, flash, redirect, url_for
from app.data_base import Products, Laptops, Orders, db

p_id = 0


@app.route('/buy/<int:product_id>/<int:quantity>')
def add_to_basket(product_id, quantity):
    global p_id
    product = Products.query.filter_by(product_id=product_id).first()
    order = Orders(foreign_key=product.product_id,
                   product_image_name=product.product_image_name,
                   product_title=product.product_title,
                   product_price=product.product_price*quantity,
                   quantity=quantity)
    db.session.add(order)
    db.session.commit()
    p_id = product_id
    print(p_id)
    return redirect(f'/product/{product_id}')


@app.route('/basket')
def show_basket():
    global p_id
    basket = Orders.query.all()
    p_id = 0
    return render_template('basket.html', basket=basket)


@app.route("/delete/<int:pr_id>")
def remove_product_from_basket(pr_id):
    order = Orders.query.filter_by(foreign_key=pr_id).first()
    db.session.delete(order)
    db.session.commit()
    return redirect('/basket')
