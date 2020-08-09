#########								#########
######### Connecting to box without SDK #########
#########								#########

import json
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import time
import secrets
import jwt
import requests

#Reading json file that was downloaded from box API while creating the app
config = json.load(open(r'path\file_3.json'))

appAuth = config["boxAppSettings"]["appAuth"]
privateKey = appAuth["privateKey"]
passphrase = appAuth["passphrase"]

# https://cryptography.io/en/latest/
key = load_pem_private_key(
  data=privateKey.encode('utf8'),
  password=passphrase.encode('utf8'),
  backend=default_backend(),
)

authentication_url = 'https://api.box.com/oauth2/token'

#print(type(config['enterpriseID']))
claims = {
  'iss': config['boxAppSettings']['clientID'],
  #'sub': config['enterpriseID'],  
  'sub': '13408298735',  #userID 
  'box_sub_type': 'user',   # 'box_sub_type': 'enterprise',
  'aud': authentication_url,
  'jti': secrets.token_hex(64),
  'exp': round(time.time()) + 45
}

keyId = config['boxAppSettings']['appAuth']['publicKeyID']

assertion = jwt.encode(
  claims,
  key,
  algorithm='RS512',
  headers={
    'kid': keyId
  }
)

params = {
    'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
    'assertion': assertion,
    'client_id': config['boxAppSettings']['clientID'],
    'client_secret': config['boxAppSettings']['clientSecret']
}
response = requests.post(authentication_url, params,verify=False)
access_token = response.json()['access_token']

print(access_token)
#access_token, refresh_token = oauth.authenticate(code)
headers = {"Authorization": f"Bearer {access_token}",'content-type': 'application/json'}
data={"name": "Test_Folder","parent":{"id":"0"}}

#Create Folder
x = requests.post('https://api.box.com/2.0/folders',data= json.dumps(data),headers=headers,verify=False)
x=requests.get('https://api.box.com/2.0/folders/0/items/',headers=headers,verify=False)
print(x.json())


#Upload File------------Getting Error in the step

headers1 = {"Authorization": f"Bearer {access_token}",'content-type':'multipart/form-data; boundary=------------------------ab85ee32db30d827','file':'string / binary'}
parent_id = '0'
data1 = { "parent_id": parent_id }
myurl = 'https://upload.box.com/api/2.0/files/content'
#myurl = 'https://upload.box.com/api/2.0/file/'
files = {'file': open(r'path\Upload.txt', 'rb')}
getdata = requests.post(myurl,data=data1,files=files,headers=headers1,verify=False)





#########							#########
######### Connecting to box with SDK#########
#########							#########


from boxsdk import JWTAuth,Client
config = JWTAuth.from_settings_file(r'path\file_3.txt')   #file_3 -> config file


#Create Folder
client = Client(config)
subfolder = client.folder('0').create_subfolder('Test_box1')

#Get List of Folders
items = client.folder(folder_id='0').get_items()
for i in items:
    print(i.name,i.id)
    
folder_id = '119922889752'

#Upload file
new_file = client.folder(folder_id).upload(r'path\Upload.txt')
print('File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id))

file_id = '702182303307'
file_content = client.file(file_id).content()


