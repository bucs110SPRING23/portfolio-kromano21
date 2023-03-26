import json
file_pointer = open("news.txt")
result = json.loads(file_pointer)
file_pointer2 = open("subs.json")
result2 = json.loads(file_pointer2)
for key, value in result2:
    if key in result:
         result[key] = result2[value]

file_pointer3 = open("betternews.txt", "w")
json.dump(result2, file_pointer3)


