#importing requests lib
import requests


#generated access token ..!!
access_token="2961628119.923c011.1fa38ef34c954f0a8cdfbee871bfd43a"

#base url which is common to all tha urls
base_url="https://api.instagram.com/v1"


#function to get the owner's info using GET
def owner_info():
    request_url = base_url+"/users/self/?access_token="+access_token
    my_info = requests.get(request_url).json()
    print "OWNER'S NAME :"+ my_info["data"]["username"]
    print  "OWNER'S IS :"+my_info["data"]["id"]



owner_info()

