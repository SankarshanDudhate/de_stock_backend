from flask import Blueprint, jsonify, request
from CustomApi.models import *

api = Blueprint("users", __name__)


@api.route('/users/<int:id>')
def user_info(id):
    return jsonify(User.query.get(id).as_dict())


@api.route('/users/<int:id>/edit', methods=['POST'])
def user_edit(id):
    user = User.query.get(id)
    data = request.form

    print(data['name'])
    print(User.query.get(id).as_dict())
    user.name = data['name']
    user.email = data['email']
    user.password = data['password']
    user.address = data['address']
    user.phoneNo = data['phoneNo']

    db.session.commit()

    return jsonify(User.query.get(id).as_dict())


@api.route('/users/create')
def create():
    return 'User Created'
