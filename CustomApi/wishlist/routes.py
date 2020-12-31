from flask import Blueprint, jsonify, request, url_for
from sqlalchemy import exc
from CustomApi.models import *
from misc_funcs import *
import json


api = Blueprint("wishlist", __name__)

@api.route('/', methods=['GET'])
def getWishlist():
	req = request.args
	user = User.query.get(req["user_id"])
	
	responseDict = {}
	if user is None:
		responseDict["Status"] = "Failure"
		print(responseDict)
		return responseDict
	
	productList = []
	wishlist = user.wishlist
	
	if wishlist:
		print("Products found!")
		wishlist = json.loads(wishlist)
		for product in wishlist:
			prod = Product.query.get(product["product_id"])
			productDict = {}
			productDict["notes"] = product["notes"] 
			productDict["product_id"] = prod.id
			productDict["product_name"] = prod.name
			productDict["product_price"] = prod.price
			category = Category.query.get(prod.category_id)
			productDict["product_category"] = category.name
			productDict["max_quantity"] = prod.maxQty
			productDict["unit"] = prod.unit
			productDict["views"] = prod.views
			productDict["details"] = prod.details
			#productDict["product_image"] = json.loads(prod.images)[0]
			#print(type(json.loads(prod.images)))
			seller = User.query.get(prod.user_id)
			productDict["seller_contact_no"] = seller.phoneNo
			productDict["quotation_received"] = None
			productDict["quotation_received"] = False
			print("user: ",req["user_id"])
			# print("product: ",prod.id)
			
			productDict["product_image"] = url_for("static", filename="images/products/" + str(prod.id) + "/0.jpg")
			
			if prod.enquiries:
				enquiries = json.loads(prod.enquiries)
				for enq in enquiries:
					if enq["buyer_id"] is req["user_id"]:
						productDict["quotation_received"] = True
						productDict["quotation"] = enq
						print("buyer: ",enq["buyer_id"])
						break
						
			productList.append(productDict)
			#print(productDict,"\n\n")
		
	else:
		print("Nothing to see here!")
			
	responseDict["Status"] = "Success"
	responseDict["products"] = productList
	print(productList)
	#return ''
	return jsonify(responseDict)
	
@api.route('/add/', methods=['POST'])
def addProduct():
	req = request.form
	user = User.query.get(req["user_id"])

	if user is None:
		return 'Not a valid user'
	
	productList = []
	productDict = {}
	productDict["product_id"] = req["product_id"]
	productDict["notes"] = req["notes"]
	
	responseDict = {}
	responseDict["Status"] = "Success"
	
	wishlist = user.wishlist
	
	if wishlist:
		wishlist = json.loads(wishlist)
		for prod in wishlist:
			productList.append(prod)
		
	productList.append(productDict)
	
	user.wishlist = json.dumps(productList)
	prod = Product.query.get(req["product_id"])
	if prod:
		prod.wishlisted = prod.wishlisted+1
		if(prod.wishlisted%1 == 0):
			prod_user = User.query.get(prod.user_id)
			fcmDeviceToken = prod_user.firebaseDeviceToken
			fcmData = {}
			fcmData["type"] = "wishlisted_count"
			fcmData["product_name"] = prod.name
			fcmData["product_image_link"] = url_for("static", filename="images/products/"+str(prod.id)+"/0.jpg")
			fcmData["wishlisted_count"] = prod.wishlisted
			fcmData["user_type"] = "seller" #notification goes to seller
			print("\n\nDevice Token: ",fcmDeviceToken,"\n")
			resp = sendFCMData(fcmDeviceToken, fcmData)
			print(resp.text)
		db.session.commit()
	else:
		responseDict["Status"] = "Failure"
		responseDict["Details"] = "Product not found!"
		
	print(productList)
	#return ''
	return jsonify(productList)


@api.route('/remove/', methods=['POST'])
def removeProduct():
	req = request.form
	user = User.query.get(req["user_id"])
	
	responseDict = {}
	if user is None:
		responseDict["Status"] = "Failure"
		print(responseDict)
		return responseDict
	
	productList = []
	wishlist = user.wishlist
	
	if wishlist:
		print("Products found!")
		
		
	return jsonify(responseDict)