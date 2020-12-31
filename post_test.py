import requests
import json
from misc_funcs import *

createNewUserImageFolderAndDummyImage(10)

#url = 'http://localhost:5000/wishlist/?user_id=1'
#myobj = {'product_id': '2', 'user_id':'1', 'notes':'Another note'}

#url = 'http://localhost:5000/wishlist/add/'
#myobj = {'product_id': '2', 'user_id':'1', 'notes':'Another note'}

#url = 'http://localhost:5000/products/enquiries/enquire/'
#myobj = {'product_id': '2', 'date':'2020-09-28', 'buyer_id':'2','enquiry':'Asking some stupid question that takes a couple of line... You wouldd think it is easy to write shit without thinking but it is not as easy as you think...','quantity':400}

url = 'http://localhost:5000/products/enquiries/reply/'
myobj = {'product_id': '1', 'date':'2020-09-22', 'buyer_id':'2','reply':'It will cost you a fortune and you can pick it up however you like. Also no time will be suitable for me.'}

#OTP endpoints
#url = 'https://2factor.in/API/V1/8b6fc480-ed2b-11ea-9fa5-0200cd936042/SMS/9881266239/AUTOGEN/Test%20Template'
#url = 'https://2factor.in/API/V1/8b6fc480-ed2b-11ea-9fa5-0200cd936042/SMS/VERIFY/f44347e6-260f-4ba8-9b9f-3ff5078dbe40/174838'


#url = 'http://localhost:5000/users/enquiries/?user_id=2'

#url = "http://192.168.43.167:5000/payments/getToken/"
#myobj = {'orderId': 'order21601909249874', 'orderAmount': 1}

# x = requests.post(url, myobj)
# print(x.text)
#
url = 'http://destock.in/test'
a = requests.get(url)
# url = 'http://192.168.43.167:5000/users/suggestions'
# b = requests.get(url)
# url = 'http://192.168.43.167:5000/products/latest'
# c = requests.get(url)
# url = 'http://192.168.43.167:5000/products/trending'
# d = requests.get(url)
# #resp = json.loads(x.text)
print(a.text)
# print(b.text)
# print(c.text)
# print(len(d.text))

#print(str(5))




'''
paymentHeaders = {'Content-Type': 'application/json', 'x-client-id': '34637a696651117db77e9bdc673643', 'x-client-secret': 'fe0548a00da63834fb420984ab248db6db105253'}
paymentData = {
 "orderId": "order2132156484842321564515613223212154561321564564",
 "orderAmount":1,
 "orderCurrency":"INR"
} 
paymentUrl = 'https://test.cashfree.com/api/v2/cftoken/order'
#resp = requests.post(paymentUrl, data=json.dumps(paymentData), headers=paymentHeaders)
#print(resp.json())
'''



'''
deviceToken = "fooFX7TBRSuh76m4iIdut6:APA91bFL6RmdyfD1zzTsu5XkS1-aeI3oNdHA4wO-SZCL5Y-fu5YwuNu5h5sbW_HnQ5G0zrxdJvKjdpiPko2krpQ4sMutvXtOtP9LPXiwkQrVAihzWlhoHltPMGE_JGlvFaiXQXyDMDoM"
notif = {"title":"Hello","body":"Red"}
data = {"click_action": "FLUTTER_NOTIFICATION_CLICK", "id": "2", "type":"wishlisted_count","user_type":"seller"}
#resp = sendFCMNotif(deviceToken, notif, data)
resp = sendFCMData(deviceToken, data)
print(resp.json())
#'''




'''
x = {"a":5}
if "a" in x:
	print(x["a"])

file = open("userImagebase64.txt","r")
content = json.dumps(file.read())
file.close()

#print(content)
writeToImage(content, "assets/user.jpg")

#file = open("base64.txt","w")
#print(content)
#file.write(content)
file.close()
'''