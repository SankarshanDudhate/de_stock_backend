from flask import Blueprint, jsonify, request
from CustomApi.models import *

api = Blueprint("products", __name__)


@api.route('/products/', methods=['GET'])
def index():
    # print(Product.query.all())
    return jsonify([product.as_dict() for product in Product.query.all()])


@api.route('/products/<int:id>/')
def show(id):
    product = Product.query.get(id)

    owner = product.owner.name
    product = product.as_dict()
    product['owner'] = owner

    return jsonify(product)


@api.route('/products/<int:id>/edit/', methods=['POST'])
def edit(id):
    product = Product.query.get(id)
    if product.owner_id == request.form['user_id']:
        product.name = request.form['name']
        product.category_id = request.form['category_id']
        product.subCategory_id = request.form['subCategory_id']
        product.available = request.form['available']

        db.session.commit()

    else:
        return jsonify("Cannot Change Product Details... You are not owner")

    return jsonify(Product.query.get(id).as_dict())


@api.route('/products/', methods=['POST'])
def search():
    if request.json:
        return 'recieved from json'

    # print(request.form['category_id'])
    return jsonify(
        [product.as_dict() for product in Product.query.filter_by(category_id=f'{request.form["category_id"]}').all()])


@api.route('/products/<path:something>/')
def error(something):
    return "URL DOES NOT EXIST"
