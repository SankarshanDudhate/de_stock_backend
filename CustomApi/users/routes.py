from flask import Blueprint, jsonify, request, url_for
from CustomApi.models import *
import json

api = Blueprint("users", __name__)


def isEmpty(listEl):
	if listEl is None:
		return True
	elif type(listEl) is list:
		if len(listEl) is 0:
			return True
		else:
			return False
	else:
		return 'Not a list!'


@api.route('/<int:id>')
def user_info(id):
	return jsonify(User.query.get(id).as_dict())


@api.route('/<int:id>/edit/', methods=['POST'])
def user_edit(id):
	user = User.query.get(id)
	data = request.form
	
	# print(data['name'])
	# print(User.query.get(id).as_dict())
	user.name = data['name']
	user.email = data['email']
	user.password = data['password']
	user.address = data['address']
	user.phoneNo = data['phoneNo']
	
	db.session.commit()
	
	return jsonify(User.query.get(id).as_dict())


@api.route('/<int:id>/profile/', methods=['GET'])
def user_profile(id):
	user = User.query.get(id)
	
	profileData = {}
	# print(user.as_dict())
	profileData['user_name'] = user.name
	profileData['user_email'] = user.email
	profileData['user_phoneNo'] = user.phoneNo
	profileData["user_image"] = url_for("static", filename="images/users/" + str(user.id) + "/user.jpg")
	
	if user.company_id > 0:
		profileData['company_exists'] = True
		company = Company.query.get(user.company_id)
		profileData['company_name'] = company.name
		profileData['panNo'] = company.pan_no
		profileData['gstNo'] = company.gst_no
		profileData['factory_address'] = company.factory_address
		profileData['office_address'] = company.office_address
		profileData['products_sold'] = company.what_you_sell
		profileData['factory_latLong'] = company.factory_latlong
	else:
		profileData['company_exists'] = False
		
	if user.contact_person_id > 0:
		# TODO doesnt work if contactPerson does not exist by default... create new for that
		profileData['contact_person_exists'] = True
		contactPerson = ContactPerson.query.get(user.contact_person_id)
		profileData['contact_person_name'] = contactPerson.name
		profileData['contact_person_email'] = contactPerson.email
		profileData['contact_person_phoneNo'] = contactPerson.phone_no
	else:
		profileData['contact_person_exists'] = False

	print("profile: ",profileData)
	return jsonify(profileData)


@api.route('/<int:id>/edit/profile/', methods=['POST'])
def user_profile_edit(id):
	user = User.query.get(id)
	data = request.form
	
	print("\n",data,"\n")
	# print(user.as_dict())
	if data["personal_details_edited"] == "true":
		print("Personal details edited")
		user.name = data['user_name']
		user.email = data['user_email']
		user.phoneNo = data['user_phoneNo']
	
	if user.company_id > 0:
		if data["company_edited"] == "true":
			print("Personal details edited")
			company = Company.query.get(user.company_id)
			company.name = data['company_name']
			company.pan_no = data['panNo']
			company.gst_no = data['gstNo']
			company.factory_address = data['factory_address']
			company.office_address = data['office_address']
			company.what_you_sell = data['products_sold']
			company.factory_latlong = json.dumps({'lat': data['factory_lat'], 'long': data['factory_long']})
	else:
		# if company has not been setup yet, create one
		company = Company(name=data['company_name'])
		company.name = data['company_name']
		company.pan_no = data['panNo']
		company.gst_no = data['gstNo']
		company.factory_address = data['factory_address']
		company.office_address = data['office_address']
		company.what_you_sell = data['products_sold']
		company.factory_latlong = json.dumps({'lat': data['factory_lat'], 'long': data['factory_long']})
		db.session.add(company)
		db.session.commit() #id would be null if we dont commit now
		print("contact person id: ", company.id)
		user.company_id = company.id
		
	if user.contact_person_id > 0:
		if data['contact_person_exists'] == "true":
			print("CP exists: ", data['contact_person_exists'])
			contactPerson = ContactPerson.query.get(user.contact_person_id)
			contactPerson.name = data['contact_person_name']
			contactPerson.email = data['contact_person_email']
			contactPerson.phone_no = data['contact_person_phoneNo']
		else:
			print("Setting contact person to 0")
			user.contact_person_id = 0
	else:
		contactPerson = ContactPerson(name=data['contact_person_name'],email=data['contact_person_email'],phone_no=data['contact_person_phoneNo'])
		db.session.add(contactPerson)
		db.session.commit() #id would be null if we dont commit now
		print("contact person id: ", contactPerson.id)
		user.contact_person_id = contactPerson.id

	db.session.commit()
	
	responseDict = {}
	responseDict["Status"] = "Success"
	
	return jsonify(responseDict)


@api.route('/<int:id>/setPassword', methods=['POST'])
def set_password(id):
	user = User.query.get(id)
	data = request.form
	# print(data)
	
	# print(User.query.get(id).as_dict())
	result = {}
	if (user.password == data['currentPassword']):
		user.password = data['newPassword']
		db.session.commit()
		result["Status"] = "Success"
		result["Details"] = "Password changed succesfully!"
	
	else:
		result["Status"] = "Failure"
		result["Details"] = "Current password entered wrong...!"
	
	return jsonify(result)


@api.route('/<int:id>/products/', methods=['GET'])
def getUsersProducts(id):
	userProdList = Product.query.filter_by(user_id=id).all()
	
	# print(userProdList)
	finalProdList = []
	for prod in userProdList:
		prodDict = prod.as_dict()
		prodDict["image"] = url_for("static", filename="images/products/" + str(prod.id) + "/0.jpg")
		# print(prodDict['expiryDate'])
		finalProdList.append(prodDict)
	
	return jsonify(finalProdList)


@api.route('/<int:id>/getTotalViews/', methods=['GET'])
def getTotalViews(id):
	userProdList = Product.query.filter_by(user_id=id).all()
	
	# print(userProdList)
	totalViews = 0
	for prod in userProdList:
		totalViews += prod.views
	
	return str(totalViews)


@api.route('/<int:id>/getActiveProductsCount/', methods=['GET'])
def getActiveProductsCount(id):
	userProdList = Product.query.filter_by(user_id=id).all()
	
	# print(userProdList)
	count = 0
	for prod in userProdList:
		if prod.expired is False:
			count += 1
	
	return str(count)


@api.route('/buyerEnquiries/', methods=['GET'])
def getBuyersEnquiries():
	req = request.args
	
	user = User.query.get(req["user_id"])
	
	responseDict = {}
	if user is None:
		responseDict["Status"] = "Failure"
		return "user does not exist!"
	
	productList = []
	productIdList = []
	
	if type(user.enquiredProducts) is str:
		productIdList = json.loads(user.enquiredProducts)
	
	if isEmpty(productIdList) is False:
		for productId in productIdList:
			prod = Product.query.get(productId)
			productDict = {}
			productDict["name"] = prod.name
			productDict["price"] = prod.price
			productDict["image"] = url_for("static", filename="images/products/" + str(prod.id) + "/0.jpg")
			
			prodCategory = Category.query.get(prod.category_id)
			productDict["category"] = prodCategory.name
			
			enquiries = prod.enquiries
			if type(enquiries) is str:
				enquiries = json.loads(
					enquiries)  # load as if it is string otherwise leave it be (mostly it will be None)
			
			# print(isEmpty(enquiries))
			# '''
			if isEmpty(enquiries) is False:
				for enq in enquiries:
					if enq["buyer_id"] is req["user_id"]:
						if "reply" in enq:
							productDict["reply"] = enq["reply"]
							prodSeller = User.query.get(prod.user_id)
							productDict["seller_image"] = url_for("static", filename="images/users/" + req[
								"user_id"] + "/user.jpg")
							productDict["seller_name"] = prodSeller.name
						
						productDict["enquiry"] = enq["enquiry"]
						productDict["quantity"] = enq["quantity"]
						break
			
			productList.append(productDict)
	
	# print(productList)
	
	responseDict["Status"] = "Success"
	responseDict["products"] = productList
	return jsonify(responseDict)


@api.route('/sellerEnquiries/', methods=['GET'])
def getSellerEnquiries():
	prodList = Product.query.filter_by(user_id=request.args["user_id"]).all()
	# print(type(prodList))
	
	productList = []
	
	if type(prodList) is list:
		for prod in prodList:
			# print(prod.enquiries)
			enquiries = prod.enquiries
			if type(enquiries) is str:
				enquiries = json.loads(
					enquiries)  # load as if it is string otherwise leave it be (mostly it will be None)
			
			# print(isEmpty(enquiries))
			# '''
			if isEmpty(enquiries) is False:
				enquiryDict = {}
				enquiryDict["id"] = prod.id
				enquiryDict["name"] = prod.name
				enquiryDict["price"] = prod.price
				enquiryDict["image"] = url_for("static", filename="images/products/" + str(prod.id) + "/0.jpg")
				# enquiryDict["image"] = ''
				# print(type(enquiries))
				
				enquiryList = []
				for enquiry in enquiries:
					# add user name and image int the enquiry data
					# print("prod id:",prod.id," --- ",enquiry["enquiry"]["user_id"])
					user = User.query.get(enquiry["buyer_id"])
					# print(enquiry)
					enquiry["buyer_name"] = user.name
					# enquiry["buyer_image"] = user.image
					enquiry["buyer_image"] = url_for("static", filename="images/users/" + str(user.id) + "/user.jpg")
					enquiryList.append(enquiry)
				
				# print(len(enquiryList), " is len")
				# print(enq)
				enquiryDict["enquiries"] = enquiryList
				
				productList.append(enquiryDict)
	# '''
	# print(len(productList))
	# return ''
	return jsonify(productList)


@api.route("/upcoming_renewals", methods=['GET'])
def upcoming_renewals():
	data = request.args
	user = User.query.get(data['user_id'])
	
	prodList = Product.query.filter_by(user_id=data["user_id"]).all()
	
	products = []
	for prod in prodList:
		# print(prod.expiryDate)
		curDate = date.today()
		delta = prod.expiryDate - curDate
		# print(delta.days)
		if delta.days <= 15:
			prodDict = {}
			prodDict["image"] = url_for("static", filename="images/products/" + str(prod.id) + "/0.jpg")
			prodDict['expiryDate'] = prod.expiryDate.strftime('%b %d, %Y')
			prodDict['id'] = prod.id
			# prodDict['randomId'] = prod.randomId
			products.append(prodDict)
	
	return jsonify(products)


@api.route("/suggestions", methods=["POST", "GET"])
def suggestions():
	# data = request.form
	# user = User.query.get(data['id'])
	user = User.query.get(1)
	# print(user.recentViews)
	suggestions = [1, 2, 3, 4, 5, 6, 7, 8]
	products = []
	for product in suggestions:
		p = Product.query.get(product)
		products.append(
			{"name": p.name, "price": p.price, "description": p.details}
		)
	print("sugeest length: ", len(products))
	return jsonify(products)


@api.route("/recent", methods=["POST", "GET"])
def recent():
	# data = request.form
	# user = User.query.get(data['id'])
	user = User.query.get(1)
	# print(user.recentViews)
	recent_views = [1, 2, 3, 4, 5, 6]
	recent_products = []
	for product in recent_views:
		p = Product.query.get(product)
		recent_products.append({"name": p.name, "price": p.price})
		
	print("recent length: ", len(recent_products))
	return jsonify(recent_products)


@api.route("/create/")
def create():
	data = request.form
	
	user = User(
		name=data["name"],
		email=data["name"],
		phoneNo=data["name"],
		password=data["name"],
		address=data["name"],
		type=data["type"],
	)
	
	return "User Created"
