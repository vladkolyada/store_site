
from app.loader import app
from flask import render_template, redirect
from app.data_base import Products, Orders, db
from .forms import Otpavka

p_id = 0
p_type = ''


@app.route('/buy/<int:product_id>/<int:quantity>/<product_type>')
def add_to_basket(product_id, quantity, product_type):
    global p_id, p_type
    product = Products.query.filter_by(product_id=product_id).first()
    orders = Orders.query.all()
    for i in orders:
        if product_id == i.foreign_key:
            i.quantity += quantity
            db.session.commit()
            break
    else:
        order = Orders(foreign_key=product.product_id,
                       product_image_name=product.product_image_name,
                       product_title=product.product_title,
                       product_price=product.product_price*quantity,
                       quantity=quantity)
        db.session.add(order)
        db.session.commit()
    p_id = product_id
    p_type = product_type
    return redirect(f'/product_{product_type}/{product_id}')


@app.route('/basket')
def show_basket():
    global p_id, p_type
    a = 0
    basket = Orders.query.all()
    p_id = 0
    for i in basket:
         a += i.product_price
    return render_template('basket.html', basket=basket, p_type=p_type, a=a)


@app.route("/delete/<int:pr_id>")
def remove_product_from_basket(pr_id):
    order = Orders.query.filter_by(foreign_key=pr_id).first()
    order.quantity -= 1
    db.session.commit()
    if order.quantity == 0:
        db.session.delete(order)
        db.session.commit()
    return redirect('/basket')


@app.route("/send_product", methods=['GET', 'POST'])
def send_prod():
    a = Otpavka()
    return render_template('otpravka_prod.html', a=a)
