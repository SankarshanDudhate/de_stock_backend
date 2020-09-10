from flask import Blueprint, jsonify, request
from CustomApi.models import *
import requests
import json

api = Blueprint("signup", __name__)


@api.route('/', methods=['POST'])
def signup():
	#TODO: check if email or phoneNo exists in db... If yes, ask user to login...
	userEmail = User.query.filter(User.email == request.form['email_id']).first()
	userPhoneNo = User.query.filter(User.phoneNo == request.form['phone_no']).first()
	
	if userEmail:
		print(userEmail)
		response = {"Status":"Failure", "Details":"Email id already exists... Please login!"}
		return jsonify(response)
	elif userPhoneNo:
		print(userPhoneNo.as_dict())
		response = {"Status":"Failure", "Details":"Phone number already exists... Please login!"}
		return jsonify(response)
	
	
	user = User(email = request.form['email_id'], password = request.form['password'], name = request.form['name'], phoneNo = request.form['phone_no'])
	db.session.add(user)
	db.session.commit()
	
	if user:
		print(user)
		print( jsonify(user.as_dict()) )
		response = { "Status":"Success", "Details":"Signed up successfully!"}
		
	else:
		#TODO show the database error in terminal... or maybe even send it to user in meaningful way...
		response = { "Status":"Failure", "Details":"Signup failed... Please try again!"}

	return jsonify(response)