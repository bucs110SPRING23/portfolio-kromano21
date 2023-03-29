import json
file_pointer = open("news.txt")
result = file_pointer.read()
file_pointer2 = open("subs.json")
result2 = json.load(file_pointer2)
for key, value in result2.items():
    newnews = result.replace(key, value)

file_pointer3 = open("betternews.txt", "w")
file_pointer3.write(newnews)


