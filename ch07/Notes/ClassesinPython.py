#Python's library contains many classes: str, int, float, bool, Turtle
#What if Python does not have a class that we need in the library?
#Create one 

#You can define a class using the class keyword
class

#You can create a new file called point.py and write your class in that file, then import the file by filename
import point

#Access classes, functions, and data in the module using the module name, then the object/function you would like to access
p1 = point.Point()
class Point:
    pass

#class: keyword
#Point: classname 
#Pass: Placeholder - do nothing 

#Self
#Because a class is a blueprint for an object and can create many objects of the same type
#we need a mechanism to know which object we are working with when inside the class
#the self keyword is a reference to the object instance that was created from the class

#class = make/model
#instance = your exploding car

#init 
#All classes have an initalizing function to tell the interpreter how to build the class
#__init__(self) is automatically called when creating the class. It constructs the objecs and gives
#its instance variables their intial values
#__init__ is called automatically anytime you create an istnace
#any function that belongs to class always has self as its first parameter. 
#Use self to refer to access atrributes of the object instance
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = "red"

#We can now create objects by calling the class
p1 = Point()
print(p1.x, p1.y, p1.color, type(p1))
p2 = Point()
print(p2.x, p2.y, p2.color, type(p2))

#Attributes - tages that tell us important things about the object
#Object attributes are variables that hold data that belongs to the object, which define its properties or characteristics
#Use the dot operator to access attributes in the object: object.attribute

#Init arguments
#What if you want to create the object with specific values
#You can pass parameters to the __init__

#Best practices
#1. One class per file
#2. Filename same as the class. all lowercase
#3. Class names should use TitleCase
