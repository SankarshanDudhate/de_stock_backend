import re

from flask import Blueprint, jsonify, request, url_for
from sqlalchemy import exc
from CustomApi.models import *
from misc_funcs import *
import json

api = Blueprint("products", __name__)


# noinspection PyPep8Naming
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


@api.route('/', methods=['GET'])
def index():
	# print(Product.query.all())
	return jsonify([product.as_dict() for product in Product.query.all()])


@api.route('/add/', methods=['POST'])
def add():
	# print(Product.query.all())
	# return jsonify([product.as_dict() for product in Product.query.all()])
	print(request.form["images"])
	return jsonify({"Status": "Success"})


@api.route('/<int:id>/')
def show(id):
	product = Product.query.get(id)
	
	productDict = product.as_dict()
	productDict['category'] = Category.query.get(product.category_id).name
	productDict['images'] = getAllProductImages(id)
	
	user = User.query.get(product.user_id)
	company_id = user.company_id
	contact_person_id = user.contact_person_id
	company = Company.query.get(company_id)
	contactPerson = ContactPerson.query.get(contact_person_id)
	productDict['company_name'] = company.name
	productDict['contact_person_name'] = contactPerson.name
	productDict['contact_person_email'] = contactPerson.email
	productDict['contact_person_phone_no'] = contactPerson.phone_no
	# print(type(product['images']))
	# print(product['images'][0])
	
	return jsonify(productDict)


@api.route('/<int:id>/editQuantity/', methods=['POST'])
def editQuantity(id):
	product = Product.query.get(id)
	data = request.form
	
	if str(product.user_id) == data['user_id']:
		product.maxQty = data['quantity']
		product.unit = data['unit']
		db.session.commit()
		
	else:
		return jsonify({"Status": "Failure", "Details": "Cannot Change Product Details... You are not owner"})
	
	return jsonify({"Status": "Success", "Details": Product.query.get(id).as_dict()})

	
@api.route('/<int:id>/edit/', methods=['POST'])
def edit(id):
	product = Product.query.get(id)
	data = request.form
	# print("\nData: ", data)
	
	if str(product.user_id) == data['user_id']:
		# print("\n", product.user_id, " : ", data['user_id'])
		product.name = data['name']
		if data['available'] is 'true':
			product.available = True
		else:
			product.available = False
		product.details = data['description']
		product.price = int(data['price'])
		product.priceDisclose = bool(data['disclosePrice'])
		product.quantity = int(data['quantity'])
		product.unit = data['unit']
		print(data['specifications'])
		product.specifications = data['specifications']
		product.latLongs = data['location_latLong']
		product.address = data['location_address']
		
		# TODO handle images
		imageList = json.loads(data['images'])
		# print(len(imageList))
		
		base_path = os.getcwd()
		staticUrl = url_for("static", filename="images/products/" + str(id) + "/")
		print("Exists: ", os.path.exists(base_path + "/CustomApi" + staticUrl))
		targetPath = base_path + "/CustomApi" + staticUrl
		# print(len(os.listdir(targetPath)))
		# print(os.listdir(targetPath))
		
		# remove store images if they were removed by user
		for storedImage in os.listdir(targetPath):
			foundFlag = False
			for receivedImage in imageList:
				receivedImage = str(receivedImage)
				if receivedImage.find(storedImage.title()) > -1:
					foundFlag = True
					break
			
			if foundFlag is False:
				storedImagePath = targetPath + '/' + storedImage
				# print(storedImagePath)
				os.remove(storedImagePath)
		
		imageCount = len(os.listdir(targetPath))
		# print(imageCount)
		
		# write base64 strings to files
		for image in imageList:
			image = str(image)  # Don't convert to lowercase here because that screws the base64 strings
			isNetworkImage = (image.lower().endswith('.jpg'))
			# print(isNetworkImage)
			
			if isNetworkImage is False:
				writeProductImage(image, id, str(imageCount) + '.jpg')
				imageCount += 1
		
		# Rename all images to maintain serial numbers (in case, 2.jpg was deleted, 3.jpg should become 2.jpg)
		currentImageNumber = 0
		# Adds '0' to all the filenames temporarily to avoid filename collisions
		for storedImage in os.listdir(targetPath):
			os.rename(targetPath + storedImage, targetPath + '0' + str(currentImageNumber) + '.jpg')
			currentImageNumber += 1
		
		# Now rename them serially
		currentImageNumber = 0
		for storedImage in os.listdir(targetPath):
			os.rename(targetPath + storedImage, targetPath + str(currentImageNumber) + '.jpg')
			currentImageNumber += 1
		
		db.session.commit()
	
	else:
		return jsonify({"Status": "Failure", "Details": "Cannot Change Product Details... You are not owner"})
	
	return jsonify({"Status": "Success", "Details": Product.query.get(id).as_dict()})

#
# @api.route('/search/', methods=['POST'])
# def search():
# 	if request.json:
# 		return 'recieved from json'
#
# 	# print(request.form['category_id'])
# 	return jsonify(
# 		[product.as_dict() for product in Product.query.filter_by(category_id=f'{request.form["category_id"]}').all()])


@api.route("/search/<int:length>/", methods=["POST"])
def searchLength(length):
	data = request.form
	# print(len(Product.query.filter(
	# 	Product.name.like('%Edwards%')
	# ).all()))
	#
	
	productList = []
	for product in Product.query.filter(Product.name.like(f'%{data["search"]}%')).all():
		productDict = product.as_dict()
		productDict['category'] = Category.query.get(product.category_id).name
		productDict["image"] = url_for("static", filename="images/products/" + str(product.id) + "/0.jpg")
		productList.append(productDict)
	
	return jsonify(
		# [   product.as_dict()
		# 	for product in Product.query.filter(
		# 	Product.name.like(f'%{data["search"]}%')
		# ).all()][length:length + 6]
		productList[length:length + 6]
	)


@api.route("/keywordSuggestion/", methods=["GET", "POST"])
def keywordSuggestion():
	# print(Product.query.all())
	if request.form["keyword"]:
		print(request.form["keyword"])
		
		# filter(Product.name.like(f'%{request.form["keyword"]}%'))
		results = []
		for word in request.form["keyword"].split(" "):
			results.extend(
				Product.query.with_entities(Product.name)
					.filter(Product.name.like(f"%{word}%"))
					.all()
			)
		
		print(results)
		
		# return jsonify([result[0] for result in results])
		
		# results = Product.filter(Product.name.like(f'%{request.form["keyword"]}%')).all()
		keywords = set()
		for word in request.form["keyword"].split(" "):
			for result in results:
				# print(result[0])
				try:
					keywords.add(
						re.search(rf"(\w*){word}(\w*)", result[0], re.I).group()
					)
				except:
					pass
		
		print(len(keywords))
		return (
			jsonify(["Cannot find"]) if len(keywords) == 0 else jsonify(list(keywords))
		)
		# return jsonify([product.as_dict() for product in
		#                 Product.query.filter(Product.name.like(f'%{request.form["keyword"]}%')).all()])
	
	# print(request.form['category_id'])
	# return jsonify(
	#     [product.as_dict() for product in Product.query.filter_by(category_id=f'{request.form["category_id"]}').all()])
	return jsonify(["Please search something"])
	
	# return jsonify([product.as_dict() for product in Product.query.all()])


@api.route("/latest", methods=["POST", "GET"])
def latest():
	# data = request.form
	# user = User.query.get(data['id'])
	# print(user.recentViews)
	latest = [1, 2, 3, 4, 5]
	latest_products = []
	for product in latest:
		p = Product.query.get(product)
		latest_products.append(
			{"name": p.name, "price": p.price, "description": p.details}
		)
	return jsonify(latest_products)


@api.route("/trending", methods=["POST", "GET"])
def trending():
	# data = request.form
	# user = User.query.get(data['id'])
	# print(user.recentViews)
	trending = [1, 2, 3, 4]
	trending_products = []
	for product in trending:
		p = Product.query.get(product)
		trending_products.append(
			{"name": p.name, "price": p.price, "description": p.details}
		)
	return jsonify(trending_products)


@api.route("/top_categories")
def top_categories():
	top = [1, 2, 3, 4, 5, 6, 7, 8]
	categories = []
	for category in top:
		c = Category.query.get(category)
		categories.append(
			{
				"name": c.name,
				"id": c.id,
				"image": url_for("static", filename=f"images/categories/{c.name}.png"),
			}
		)
	return jsonify(categories)


@api.route("/all_categories")
def all_categories():
	categories = Category.query.all()
	
	response = []
	for category in categories:
		response.append(
			{
				"name": category.name,
				"id": category.id,
				"image": url_for(
					"static", filename=f"images/categories/{category.name}.png"
				),
			}
		)
	return jsonify(response)


@api.route('/enquiries/enquire/', methods=['POST'])
def enquire():
	# print(request.form)
	prod = Product.query.get(request.form["product_id"])
	# print(type(prod))
	
	enquiryList = []
	
	# noinspection PyDictCreation
	responseDict = {}
	responseDict["Status"] = "Success"
	
	enquiryDict = {}
	enquiryDict["enquiry"] = request.form["enquiry"]
	enquiryDict["buyer_id"] = request.form["buyer_id"]
	enquiryDict["date"] = request.form["date"]
	enquiryDict["replied"] = False
	enquiryDict["quantity"] = request.form["quantity"] + " " + prod.unit
	# print(enquiryDict)
	
	fcmData = {}
	fcmData["type"] = "enquiry"
	fcmData["enquiry"] = request.form["enquiry"]
	fcmData["quantity"] = request.form["quantity"] + " " + prod.unit
	
	enquiryFoundFlag = False
	
	if prod:
		fcmData["product_name"] = prod.name
		fcmData["product_id"] = prod.id
		enquiries = prod.enquiries
		if type(prod.enquiries) is str:
			enquiries = json.loads(
				enquiries)  # load as json if it is string otherwise leave it be (mostly it will be None)
		
		# print(enquiries)
		
		if isEmpty(enquiries) is False:
			for enquiry in enquiries:
				if enquiry["buyer_id"] is request.form["buyer_id"]:
					enquiry = enquiryDict
					enquiryFoundFlag = True
				
				enquiryList.append(enquiry)
			
			if enquiryFoundFlag is False:
				enquiryList.append(enquiryDict)
		
		else:
			enquiryList.append(enquiryDict)
		
		prod.enquiries = json.dumps(enquiryList)
		enquiredFlag = False
		
		user = User.query.get(request.form["buyer_id"])
		
		fcmData["user_name"] = user.name
		fcmData["user_image_link"] = url_for("static",
		                                     filename="images/users/" + request.form["buyer_id"] + "/user.jpg")
		fcmData["product_image_link"] = url_for("static", filename="images/products/" + str(prod.id) + "/0.jpg")
		fcmData["user_type"] = user.type
		# print("URL: ",url_for("users.create"))
		fcmDeviceToken = user.firebaseDeviceToken
		
		userEnquiredProducts = user.enquiredProducts
		enquiredProducts = []
		
		if userEnquiredProducts:
			userEnquiredProducts = json.loads(userEnquiredProducts)
			for productId in userEnquiredProducts:
				if productId is request.form["product_id"]:
					enquiredFlag = True
					break
				else:
					# print('')
					enquiredProducts.append(productId)
			
			if enquiredFlag is True:
				# It means product has already been enquired by user
				# print('found true')
				enquiredProducts = userEnquiredProducts
			else:
				enquiredProducts.append(request.form["product_id"])
		else:
			enquiredProducts.append(request.form["product_id"])
		
		user.enquiredProducts = json.dumps(enquiredProducts)
		# print("enquired for ",enquiredProducts)
		db.session.commit()
		
		# fcmNotif = {"title": "New Enquiry", "body": "Product: "+prod.name}
		resp = sendFCMData(fcmDeviceToken, fcmData)
		print("Notif response\n", resp.json(), "\n\n")
	# print(enquiryList)
	# print(prod.enquiries)
	# return ''
	# return prod.enquiries
	return jsonify(responseDict)


@api.route('/enquiries/reply/', methods=['POST'])
def replyToEnquiry():
	# print(request.form)
	prod = Product.query.get(request.form["product_id"])
	# print(type(prod))
	enquiryList = []
	responseDict = {}
	responseDict["Status"] = "Success"
	
	fcmData = {}
	fcmData["type"] = "reply"
	fcmData["reply"] = request.form["reply"]
	
	if prod:
		fcmData["product_name"] = prod.name
		enquiries = json.loads(prod.enquiries)
		print(enquiries, "\n--------\n")
		print(prod.enquiries)
		for enquiry in enquiries:
			# print(enquiry,"\n-----------\n")
			if (enquiry["buyer_id"] == request.form["buyer_id"]):
				replyDict = {}
				# replyDict["seller_id"] = prod.user_id #seems redundant as you can always use prod.user_id
				replyDict["date"] = request.form["date"]
				replyDict["seller_reply"] = request.form["reply"]
				enquiry["reply"] = replyDict
				enquiry["replied"] = True
			enquiryList.append(enquiry)
		
		try:
			prod.enquiries = json.dumps(
				enquiryList)  # json.loads conveerts python types like True to json types like true
			db.session.commit()
		except exc.SQLAlchemyError:
			responseDict["Status"] = "Failure"
			return jsonify(responseDict)
		
		user = User.query.get(prod.user_id)
		fcmData["user_name"] = user.name
		fcmDeviceToken = user.firebaseDeviceToken
		fcmData["user_type"] = "buyer"
		fcmData["user_image_link"] = url_for("static", filename="images/users/" + str(user.id) + "/user.jpg")
		fcmData["product_image_link"] = url_for("static", filename="images/products/" + str(prod.id) + "/0.jpg")
		resp = sendFCMData(fcmDeviceToken, fcmData)
		print("\n", resp.json(), "\n")
	
	print(enquiryList)
	# print(prod.enquiries)
	# return ''
	# return prod.enquiries
	return jsonify(responseDict)


@api.route('/<path:something>/')
def error(something):
	return "URL DOES NOT EXIST"


@api.route("/<int:product_id>/images/", methods=['GET'])
def getAllProductImages(product_id):
	base_path = os.getcwd()
	# print(base_path)
	staticUrl = url_for("static", filename="images/products/" + str(product_id) + "/")
	
	staticUrlNorm = os.path.normpath(staticUrl)  # Converts slashes if needed
	# print(os.path.exists(base_path + "\CustomApi" + staticUrl))
	targetPath = base_path + "\CustomApi" + staticUrlNorm
	# print(len(os.listdir(targetPath)))
	# print(os.listdir(targetPath))
	
	imageLinks = []
	for img in os.listdir(targetPath):
		print(img.title())
		imageLinks.append(staticUrl + img.title())
	
	print(json.dumps(imageLinks))
	return imageLinks
