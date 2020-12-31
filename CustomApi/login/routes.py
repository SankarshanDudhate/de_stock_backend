from flask import Blueprint, jsonify, request
from CustomApi.models import *
import requests
import json

api = Blueprint("login", __name__)


@api.route('/', methods=['POST'])
def login():
	emailOrNumber = 'email_id' in request.form
	
	if emailOrNumber:
		user = User.query.filter(User.email == request.form['email_id'], User.password == request.form['password']).first()
	else:
		user = User.query.filter(User.phoneNo == request.form['phone_no'], (User.password == request.form['password'])).first()
		
	result = {}
	if user:
		#print(user)
		result["Status"] = "Success"
		result["Details"] = "Login successful!"
		result["userData"] = user.as_dict()
		print( user.as_dict() )
		return jsonify(result)
	else:
		result["Status"] = "Failure"
		result["Details"] = "Login unsuccessful... Please check your credentials!"
		return jsonify(result)