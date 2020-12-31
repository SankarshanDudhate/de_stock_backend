import json

from flask import Blueprint, jsonify, request, url_for, render_template, current_app
import os

api = Blueprint("images", __name__)

@api.route('/user/<int:user_id>/', methods=['GET'])
def getUserImage(user_id):
	imgUrl = url_for('static', filename='images/users/'+str(user_id)+'user.jpg')
	print(imgUrl)
	# return '<img src=' + url_for("static", filename="user.jpg") + '>'
	return imgUrl
