from app.loader import app
from flask import render_template, redirect
from app.data_base import Products, Orders, db

p_id = 0
p_type = ''
total_sum = 0


@app.route('/buy/<int:product_id>/<int:quantity>/<product_type>')
def add_to_basket(product_id, quantity, product_type):
    global p_id, p_type, total_sum
    product = Products.query.filter_by(product_id=product_id).first()
    order = Orders(foreign_key=product.product_id,
                   product_image_name=product.product_image_name,
                   product_title=product.product_title,
                   product_price=product.product_price*quantity,
                   quantity=quantity)
    db.session.add(order)
    db.session.commit()
    p_id = product_id
    p_type = product_type
    total_sum += product.product_price*quantity
    return redirect(f'/product_{product_type}/{product_id}')


@app.route('/basket')
def show_basket():
    global p_id, p_type, total_sum
    basket = Orders.query.all()
    p_id = 0
    return render_template('basket.html', basket=basket, p_type=p_type, total_sum=total_sum)


@app.route("/delete/<int:pr_id>")
def remove_product_from_basket(pr_id):
    order = Orders.query.filter_by(foreign_key=pr_id).first()
    db.session.delete(order)
    db.session.commit()
    return redirect('/basket')
