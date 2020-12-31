import shutil

import requests
import json
import base64
import os
from flask import url_for

base_path = os.getcwd()
staticImagesFolderPath = "/static/images"
imagesFolderAbsolutePath = base_path + "/CustomApi" + staticImagesFolderPath

def createNewUserImageFolderAndDummyImage(userId):
	print("Creating folder for user id: ", userId)
	usersFolderAbsolutePath = imagesFolderAbsolutePath+'/users/'
	dummyImagePath = usersFolderAbsolutePath+'userDummy.jpg'
	folderExists = os.path.exists(usersFolderAbsolutePath + '/' + str(userId))
	print("Exists: ", folderExists)
	if folderExists is False:
		os.mkdir(usersFolderAbsolutePath + str(userId))
	copyToPath = usersFolderAbsolutePath+str(userId)+'/user.jpg'
	shutil.copy2(dummyImagePath, copyToPath)

def writeToImage(imgString, filepath):
	imgdata = base64.b64decode(imgString)
	#use base64.b64encode(image_file.read()) to get image's base64 string
	#filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
	with open(filepath, 'wb') as imageFile:
		imageFile.write(imgdata)
		
def writeProductImage(image, productId, filename):
	absoluteImagePath = imagesFolderAbsolutePath + "products/" + str(productId) + '/' + filename
	# print(absoluteImagePath)
	# print(os.path.exists(absoluteImagePath))
	writeToImage(image, absoluteImagePath)
	

#Don't use this one... use sendFCMData() instead
def sendFCMNotif(_deviceToken, _notif, _data):
	serverToken = "AAAAAcff4vI:APA91bFkwA3YQa9VyNSM6eeYB9w_ZENxoWEFXT5_l0I2R09nooO9bQKZblQoPvtJZVXWlKuTNEe-wowuVeSzjJxeq8A3j_ozyC7a9mmwijNObNu7RY6g7_5I_58CgHr7W_z16FJdJEiy"
	fcmUrl = "https://fcm.googleapis.com/fcm/send"
	fcmHeaders = {
	'Content-Type': 'application/json',
	'Authorization': 'key=' + serverToken,
	}
	
	#Norification format
	#notif = {"title":"Hello","body":"Red"}
	_data["click_action"] = "FLUTTER_NOTIFICATION_CLICK"
	fcmBody = {"to": _deviceToken,"notification": _notif, "data": _data}

	response = requests.post(fcmUrl, data=json.dumps(fcmBody), headers=fcmHeaders)
	#print(response.text)
	return response

def sendFCMData(_deviceToken, _data):
	serverToken = "AAAAAcff4vI:APA91bFkwA3YQa9VyNSM6eeYB9w_ZENxoWEFXT5_l0I2R09nooO9bQKZblQoPvtJZVXWlKuTNEe-wowuVeSzjJxeq8A3j_ozyC7a9mmwijNObNu7RY6g7_5I_58CgHr7W_z16FJdJEiy"
	fcmUrl = "https://fcm.googleapis.com/fcm/send"
	fcmHeaders = {
	'Content-Type': 'application/json',
	'Authorization': 'key=' + serverToken,
	}
	
	#Norification format
	#notif = {"title":"Hello","body":"Red"}
	_data["click_action"] = "FLUTTER_NOTIFICATION_CLICK"
	fcmBody = {"to": _deviceToken, "data": _data}

	response = requests.post(fcmUrl, data=json.dumps(fcmBody), headers=fcmHeaders)
	#print(response.text)
	return response
