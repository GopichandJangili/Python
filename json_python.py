#JSON is JavaScript Object Notation
import json
import os

#get current working directory
print(os.getcwd())

a = {'k1':1,'k2':2}
#converting to json is done by dummps function
c = json.dumps(a)
print(type(c),c)


#read from json file
with open(os.path.join(os.getcwd(),'Input.json')) as json_1:
    c = json.load(json_1)

print(c)


json_decoded = {'a':1,'b':2}
#write to json file
with open(os.path.join(os.getcwd(),'Data.json'),'w') as json_file:
     json.dump(json_decoded,json_file) 

