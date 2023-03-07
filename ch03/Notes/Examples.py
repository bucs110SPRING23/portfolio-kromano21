#Iteration
#Iterable - you can loop over it

mystr = "hello"
#iterable list of characters
mynums = [1, 2, 3, 4, 5]

for ch in mystr:
    print(ch)

for num in mynums:
    print(num)

#Anything iterable can be "indexed" into
print(mystr[0], mystr[1], mystr[2], mystr[3], mystr[4])

mynums [0] = 5 #mutable = changeable
print(mynums)
#immutable = can't be changed once created

num = 5 
mystr = "hello" #immutable 

mynums = [1, 2, 3, 4, 5] #mutable
myothernums = [1, 2, 3, 4, 5] #mutable

mystr = "hello" #immutable
myotherstring = "hello" #immutable. Python treats string as immutable objects so mystr and myotherstring is the same thing. 

if mynums is myothernums: 
    print("They are the same")
#Will not print because python identifies these as two different objects since they are mutable

#substring
mystr = "hello"
print(mystr[0])
print(mystr[1:4])
#prints h ell

mystr2 = mystr[1:5]
print(mystr, mystr2)
#not modifying the orginal string, just returning a new version of that string (temporary version?)
#Iterable objects are not always mutable 

#slicing with mutable objects
mynums = [1, 2, 3, 4, 5]

mynums[2:2] = [2.5, 2.6]
print(mynums)

mynums[3:3] = [2.5, 2.6]
for i in mynums:
    print(i)

contacts = [
    ["bill", "867-5309"],
    ["jane", "555-1212"],
]
#worse case scenario: Looping n times, where n is the number of times 
name = input("Enter a name: ")

for contact in contacts:
    if contact[0] == name:
        print(contact[1])
        break

#relationship index => value
#NOT VALID PYTHON
contact = [   "[" ] #was not closed
#    "bill": "867-5309",
#    "jane": "555-1212",
#]

print(contact[name])
#dictionary
contact = {
    "bill": "867-5309",
    "jane": "555-1212",
}
print(contact["jane"])
print(contact["joe"])

#list[index] = value
#dictionary[key] = value
# key/value pairs
# keys must be unique
# keys must be immutable 