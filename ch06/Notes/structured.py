#Protocols 
# - http #sending strings over a network
# - xml 
# json #javascript object notation 
#sending structured data
#string formats, not file formats 
#int, float, string, bool, list, dictionary, None
#^only options for data types
# {}:dictionary, []: list

import json

data = {
    "num": 1, 
    "msg": "Hello World",
}

json_string = json.dumps(data)
print(json_string, type(json_string))

json_data = json.loads(json_string)

for k, v in json_data.items():
    print(k, v)

fptr = open("assets/data.json", "w") #json is a convention, it's not a file type
fptr.write(json_string)
fptr.close()

fptr = open("assets/data.json", "r").read()
data_str = open