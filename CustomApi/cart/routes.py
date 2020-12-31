from flask import Blueprint, jsonify, request
from CustomApi.models import *

api = Blueprint("cart", __name__)


@api.route('/', methods=['post'])
def list_all():
    cart = Cart.query.filter(Cart.user_id == request.form['user_id']).first()
    return jsonify(cart.product_ids)
    pass


@api.route('/add', methods=['post'])
def add():
    cart = Cart.query.filter(Cart.user_id == request.form['user_id']).first()

    if not cart:
        print('New Cart initialised')
        new_cart = Cart(user_id=request.form['user_id'], product_ids=request.form['product_id'])
        db.session.add(new_cart)
        db.session.commit()

        cart = Cart.query.filter(Cart.user_id == request.form['user_id']).first()

    products = cart.product_ids.split(',')

    if str(request.form['product_id']) not in products:
        products.append(str(request.form['product_id']))
        cart.product_ids = ','.join(products)
        db.session.commit()

    print(cart.product_ids)

    return jsonify('1')


@api.route('/remove', methods=['post'])
def remove():
    # user = User.query.filter(request.form['user_id'])
    # product = Product.query.filter(Product.id == request.form['product_id'])
    cart = Cart.query.filter(Cart.user_id == request.form['user_id']).first()
    cart_list = cart.product_ids.split(',')
    cart_list.remove(request.form['product_id'])
    cart.product_ids = ','.join(cart_list)
    db.session.commit()
    return jsonify(cart.product_ids)
    pass


@api.route('/total')
def total():
    pass
