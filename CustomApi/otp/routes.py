from flask import Blueprint, jsonify, request
from CustomApi.models import *
import requests
import json

api = Blueprint("otp", __name__)


@api.route('/send', methods=['post'])
def sendOTP():
	phone_no = 'phone_no' in request.form
		
	#OTP endpoints
	#url = 'https://2factor.in/API/V1/8b6fc480-ed2b-11ea-9fa5-0200cd936042/SMS/9881266239/AUTOGEN'
	#url = 'https://2factor.in/API/V1/8b6fc480-ed2b-11ea-9fa5-0200cd936042/SMS/VERIFY/77d9fb18-69e9-4a4b-8225-728a7a5c0d45/665997'

	otpUrl = 'https://2factor.in/API/V1/8b6fc480-ed2b-11ea-9fa5-0200cd936042/SMS/'+request.form['phone_no']+'/AUTOGEN/Test%20Template'
	resp = requests.get(otpUrl)
	resp = json.loads(resp.text)
	#return jsonify(request.form)
	return jsonify(resp)
	
@api.route('/verify', methods=['post'])
def remove():
	otp = 'otp' in request.form
	sessionId = 'session_id' in request.form
	
	otpUrl = 'https://2factor.in/API/V1/8b6fc480-ed2b-11ea-9fa5-0200cd936042/SMS/VERIFY/'+request.form['session_id']+'/'+request.form['otp']
	print(otpUrl)
	resp = requests.get(otpUrl)
	resp = json.loads(resp.text)
	return jsonify(resp)
