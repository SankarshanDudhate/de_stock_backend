import base64
import hashlib
import hmac

from flask import Blueprint, jsonify, request
from CustomApi.models import *
import requests
import json

from misc_funcs import *

api = Blueprint("signup", __name__)


@api.route('/', methods=['POST'])
def signup():
	#TODO: check if email or phoneNo exists in db... If yes, ask user to login...
	data = request.form
	userEmail = User.query.filter(User.email == data['email_id']).first()
	userPhoneNo = User.query.filter(User.phoneNo == data['phone_no']).first()
	
	if userEmail:
		print(userEmail)
		response = {"Status":"Failure", "Details":"Email id already exists... Please login!"}
		return jsonify(response)
	elif userPhoneNo:
		print(userPhoneNo.as_dict())
		response = {"Status":"Failure", "Details":"Phone number already exists... Please login!"}
		return jsonify(response)
	
	secretKey = bytes("fooFX7TBRSuh76m4iIdut6:APA91bFL6RmdyfD1zzTsu5XkS1", encoding='utf-8')
	hashMessage = bytes(data['name'] + data['email_id'] + data['phone_no'], encoding='utf-8')
	calculatedHash = base64.b64encode(hmac.new(secretKey, hashMessage, digestmod=hashlib.sha256).digest()).decode(
		'utf-8')
	
	user = User(email = data['email_id'], password = data['password'], name = data['name'], phoneNo = data['phone_no'])
	user.firebaseDeviceToken = data['firebaseDeviceToken']
	print(user.firebaseDeviceToken)
	user.shareableKey = calculatedHash
	db.session.add(user)
	db.session.commit()
	
	if user:
		print(user)
		print( jsonify(user.as_dict()) )
		createNewUserImageFolderAndDummyImage(user.id)
		response = { "Status":"Success", "Details":"Signed up successfully!"}
		response["Data"] = {"user_id": user.id, "shareableKey": user.shareableKey, "email": user.email, "name": user.name, "phoneNo": user.phoneNo}
		
	else:
		#TODO show the database error in terminal... or maybe even send it to user in meaningful way...
		response = { "Status":"Failure", "Details":"Signup failed... Please try again!"}
		
	#TODO create user folder in images and copy a dummy image there

	return jsonify(response)