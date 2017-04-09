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

#funcion gets user information by using there user name
def get_user_info_by_username(user_name):
    user_url = base_url+"/users/search?q=="+user_name+"&access_token="+access_token
    user_info = requests.get(user_url).json()
    print user_info["data"][0]["username"]
    print user_info["data"][0]["full_name"]
    return user_info["data"][0]["id"]

#function calling
#get_user_info_by_username("badshahking143")

#function to return post id by taking post_number and user_name as an argument
def get_user_post_id(user_name,post_number):
    i=post_number
    user_id = get_user_info_by_username(user_name)
    url_id = base_url+"/users/"+user_id+"/media/recent/?access_token="+access_token
    rqst_url=requests.get(url_id).json()
    return rqst_url["data"][i]["id"]

#function calling
#print get_user_post_id("badshahking143",1)


