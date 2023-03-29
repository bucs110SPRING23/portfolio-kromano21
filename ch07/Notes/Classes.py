import random
import turtle
#Class = type
#class are named with TitleCase
#class won't change, things that are constant usually start with an uppercase letter
class Point:
    "docstring for Point"

    #functions are called 'methods' when they are in a class
    #first parameter to any method is "self"
    def_init_(self, x = 0, y = 0, color = "red"): #for Python's use
        self.xcoor = x
        self.ycoor = y
        self.color = color

#Then import point
#When doing so it will
#1. Look in the current folder for the file/module 
#2. Look in python installed modules 
#3. Look in the python library 
import sub.module #import something specifically 

# - snakecase: snake_case, underscores for spaces, all lowercase
# - Camelcase: camelCase, capital for spaces, starts lowercase 
# - TitleCase: capital for spaces, starts capital - typically for something that never changes
p1.xcoor = 10


print(p1.xcoor, p1.ycoor, p1.color, type(p1), id(p1))
print(p2.xcoor, p2.ycoor, p2.color, type(p2), id(p2))

points = []
for p in range(10):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    points.append(point.Point(x, y, "orange"))


turtle = turtle.Turtle()
for p in points:
    t.color(p.color)
    t.goto(p.xcoor, p.ycoor)

turtle.Screen().exitonclick()

#Classes break up a program into smaller modules 