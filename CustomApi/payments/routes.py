from flask import Blueprint, jsonify, request, url_for
from sqlalchemy import exc
from CustomApi.models import *
from misc_funcs import *
import json
import hashlib
import hmac
import base64

api = Blueprint("payments", __name__)


@api.route('/getTestToken/', methods=['POST'])
def getTestToken():
	print("POST DATA")
	test_appid = '34637a696651117db77e9bdc673643'
	test_secret = "fe0548a00da63834fb420984ab248db6db105253"
	
	paymentHeaders = {'Content-Type': 'application/json', 'x-client-id': test_appid, 'x-client-secret': test_secret}
	paymentData = {
		"orderId": request.form["orderId"],
		"orderAmount": request.form["orderAmount"],
		"orderCurrency": "INR"
	}
	
	testPaymentUrl = 'https://test.cashfree.com/api/v2/cftoken/order'
	resp = requests.post(testPaymentUrl, data=json.dumps(paymentData), headers=paymentHeaders)
	print(resp.json())
	return resp.text


@api.route('/getToken/', methods=['POST'])
def getToken():
	print("POST DATA")
	prod_secret = "9e2e2cf8f10b8ba78172adfc2eae8792663cf23d"
	prod_appid = "793036fb9dc8738c0d594aa4530397"
	paymentHeaders = {'Content-Type': 'application/json', 'x-client-id': prod_appid, 'x-client-secret': prod_secret}
	paymentData = {
		"orderId": request.form["orderId"],
		"orderAmount": request.form["orderAmount"],
		"orderCurrency": "INR"
	}
	
	prodPaymentUrl = 'https://api.cashfree.com/api/v2/cftoken/order'
	resp = requests.post(prodPaymentUrl, data=json.dumps(paymentData), headers=paymentHeaders)
	print(resp.json())
	return resp.text


@api.route('/webhook/', methods=['GET', 'POST'])
def webhook_receiver():
	# This creates file if it does not exist, to avoid errors
	file = open("payment_data.txt", "a")
	file.close()
	
	if request.method == 'GET':
		file = open("payment_data.txt", "r")
		contents = file.read()
		print("Webhook File previous contents: ", contents)
		file.close()
		return contents
	
	else:
		file = open("payment_data.txt", "a")
		
		postData = {
			"orderId": request.form['orderId'],
			"orderAmount": request.form['orderAmount'],
			"referenceId": request.form['referenceId'],
			"txStatus": request.form['txStatus'],
			"paymentMode": request.form['paymentMode'],
			"txMsg": request.form['txMsg'],
			"signature": request.form['signature'],
			"txTime": request.form['txTime']
		}
		
		print("POST DATA: ", postData)
		file.write(json.dumps(postData))
		file.close()
	
	return 'POST DATA'


@api.route('/verifyTestSignature/', methods=['POST'])
def verifyTestSignature():
	req = request.form
	
	postData = {
		"orderId": request.form['orderId'],
		"orderAmount": request.form['orderAmount'],
		"referenceId": request.form['referenceId'],
		"txStatus": request.form['txStatus'],
		"paymentMode": request.form['paymentMode'],
		"txMsg": request.form['txMsg'],
		"signature": request.form['signature'],
		"txTime": request.form['txTime']
	}
	
	responseJson = {"Status": "Success"}
	
	signatureData = ""
	signatureData = postData['orderId'] + postData['orderAmount'] + postData['referenceId'] + postData['txStatus'] + \
	                postData['paymentMode'] + postData['txMsg'] + postData['txTime']
	
	test_secret = "fe0548a00da63834fb420984ab248db6db105253"
	
	message = bytes(signatureData, encoding='utf-8')  # .encode('utf-8')
	secret = bytes(test_secret, encoding='utf-8')  # .encode('utf-8')
	calculatedSignature = base64.b64encode(hmac.new(secret,
	                                                message, digestmod=hashlib.sha256).digest()).decode('utf-8')
	
	if calculatedSignature == postData["signature"]:
		print("Signatures matched: ", calculatedSignature, ", ", postData["signature"])
	else:
		print("Signature mismatch, ", calculatedSignature == postData["signature"])
		responseJson = {"Status": "Failure"}
		return responseJson
	
	file = open("payment_data.txt", "a+")
	# content = json.dumps(file.read())
	print("File previous contents: ", file.read())
	file.write(json.dumps(postData) + ",\n")
	file.close()
	
	return jsonify(responseJson)


# Can eliminate this endpoint by passing a parameter to above function - like, /verifySignature/(test/prod)
@api.route('/verifySignature/', methods=['POST'])
def verifySignature():
	req = request.form
	
	postData = {
		"orderId": request.form['orderId'],
		"orderAmount": request.form['orderAmount'],
		"referenceId": request.form['referenceId'],
		"txStatus": request.form['txStatus'],
		"paymentMode": request.form['paymentMode'],
		"txMsg": request.form['txMsg'],
		"signature": request.form['signature'],
		"txTime": request.form['txTime']
	}
	
	responseJson = {"Status": "Success"}
	
	signatureData = ""
	signatureData = postData['orderId'] + postData['orderAmount'] + postData['referenceId'] + postData['txStatus'] + \
	                postData['paymentMode'] + postData['txMsg'] + postData['txTime']
	
	prod_secret = "9e2e2cf8f10b8ba78172adfc2eae8792663cf23d"
	
	message = bytes(signatureData, encoding='utf-8')  # .encode('utf-8')
	secret = bytes(prod_secret, encoding='utf-8')  # .encode('utf-8')
	calculatedSignature = base64.b64encode(hmac.new(secret,
	                                                message, digestmod=hashlib.sha256).digest()).decode('utf-8')
	
	if calculatedSignature == postData["signature"]:
		print("Signatures matched: ", calculatedSignature, ", ", postData["signature"])
	else:
		print("Signature mismatch, ", calculatedSignature == postData["signature"])
		responseJson = {"Status": "Failure"}
		return responseJson
	
	file = open("payment_data.txt", "a+")
	# content = json.dumps(file.read())
	print("File previous contents: ", file.read())
	file.write(json.dumps(postData) + ",\n")
	file.close()
	
	return jsonify(responseJson)


@api.route('/save_temp_products/', methods=['POST'])
def saveTempProducts():
	data = request.form
	
	userTempProductsData = TempProduct.query.filter_by(user_id=data['user_id']).first()
	print(json.loads(data['products']))
	
	if userTempProductsData is None:
		print("Creating new temp prod row")
		temp_prod = TempProduct(products=json.loads(data['products']), user_id=data['user_id'])
		db.session.add(temp_prod)
	
	else:
		print("Editing temp prod data")
		userTempProductsData.products = data['products']
	
	db.session.commit()
	
	return jsonify({"Status": "Success"})

@api.route('/publish_products/', methods=['POST'])
def publishProducts():
	data = request.form
	return
