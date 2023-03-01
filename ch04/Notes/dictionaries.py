#Dictionaries 
#Suppose you want to store names and phone numbers in a program
contacts = [
    ["Luke", "657-6789"],
    ["Leia", "568-9970"],
    ["Han", "645-7897"]
]
#To look someone up, you would have to write the following code
name = input("Who's number do you want? ")
for contact in contacts:
    if contact[0] == name:
        print(contact[1])
#Problem: The index of the list object has no relationship with the value of the object
#An object's index is determined by insertion order only 
contacts = [
    0:["Luke", "657-6789"],
    1:["Leia", "568-9970"],
    2:["Han", "645-7897"]
]
#How Could we Change the Index to be relevant to the Value?
contacts = [
    "Luke":["Luke", "657-6789"],
    "Leia":["Leia", "568-9970"],
    "Han":["Han", "645-7897"]
]

name = input("Who's number do you want? ")
print(contact[name])
#instead of an index, we call it a key now because objects are retrieved by some meaningful ID, not in linear order
#Dictionaires use key/value to manage objects 
defined with: {}
#Key Requirements:
#Any immutable object (str, int, tuple, etc)
#unique to the dictionary 
contacts = {}
contacts["Luke"] ="657-6789"
contacts["Leia"] = "568-9970"
contacts["Han"] = "645-7897"

contacts["Han"] = ""
}
#If key exists: update value
#If key does not exist: insert key/value 
#.items()
for i in contacts:
    print(i)
    print(contacts[1])
#When iterating through a dictionary, the iterating variable is the key, not the value
#The dictionary method .items() returns a list of tuples consisting of key/value pairs
#items() works kind of like enumerate() for dictionaries
contacts = {
    "Luke":"657-6789",
    "Leia":"568-9970",
    "Han":"645-7897"
}

print(list(contacts.items()))
for k,v in contacts.items():
    print(k, ":", v)
#.get(): What happens when you try to access a key not in the dictionary
contacts = {
    "Luke":"657-6789",
    "Leia":"568-9970",
    "Han":"645-7897"
}
#print(contacts["chewbacca"]) ERROR

#we can use get() instead to access elements of a dictionary 
value = contacts.get("chewbacca")
print(value)

if contacts.get("chewbacca"): #returns `None` if not in the dictionary
    print(contacts["chewbacca"])
else:
    print("Not in the address book")

#Addtionally, an optional second argument allows you to set a default value if the key doesn't exist 
result = contacts.get("chewbacca", "Not in the address book") #Use second default parameter
print(result)

#Iterable Objects
#Strings: immutable, have methods (commands), slicing
#Lists: mutable, have methods, slicing 
#Tuples: immutable, lightweight lists
#Dictionary: mutable, key/value pairs, keys must be immutable, no slicing
