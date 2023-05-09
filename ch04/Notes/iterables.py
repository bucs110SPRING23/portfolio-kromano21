#To access objects in a list, we can iterate through them 
#Any object is iterable if you can traverse through all of its given values one by one 

#Is Str an iterable?
#the object in a for loop is iterable 

#String Manipulation
#Immutable: Cannot be changed once created 
#Mutable: Can be changed after creating the object
#Str is an immutable object
#String methods always return a copy 

#Substrings
#apple -> app
#You can get a substring using the slice operator
#mystr[start:end]
#Start is inclusive, end is exclusive

#List Iteration
#You can change the objects in a list
#dessert = ["chocolate", "strawberry", "vanilla"]
#dessert[3:3] = ["mocha"] #Substring Format. 
#dessert[1:3] = ["caramel", "raspberry"] #1 is inclusive but 3 is not inclusive
#print(dessert)

#Enumerate 
#To alter the original list object in a for loop, use enumerate
#Enumerate() creates two values from your list: (index, value)
#i: index
#obj: a copy of the actual object 
mylist = [1, 2, 3, 4]
for i, obj in enumerate(mylist):
    mylist[i] = "Better Robots"
print(mylist)
#Now we are accessing the actual element and can make changes