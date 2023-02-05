var1_data = 1
print(var1_data + 6)
print(var1_data + 6)
print(var1_data + 3467)

#"1" - string
#1 - integer

var1_data = "7"
print(type(var1_data))

print(7, "7")#types
#Variables like a bucket of data
- put things in 
- Take things out
- pass them around 
numbers, letters, underscores, no spaces, must start with a lowercase letter

'=': assingment operator, programmers refer to it as equal 
#3 data types of Python = int, flow, string
#container types
- data that only holds other data 
#list
mylist = [1, "2", 3, 4.0, [5, 6, 7, 8, 9, 10]]
#can insert different types inside the same list ^
#can create a list inside of a list^

print(mylist[0]) #0 indexed
print(mylist[2])
print(mylist[-1])
print(mylist[-2])
#print(mylist[8]) #ERROR

#can break a list across multiple lines 
mycolors = [
    "red",
    "green",
    "blue"
]

print(mycolors, len(mycolors))

mycolors[1] = "purple"
#changes green because first entry is 0 

#add yellow
mycolors.append("yellow")
print(mycolors)
#delete color
del mycolors[2]

var = 4
print(str(var)+ " is a number")
print(float(var) " is a number")

var = 4.0
float(var)
int(var) #error
'str': text, uses "" or ''
'int': whole number

#module - a fancy name for a python file 
'print()'
'input()'
'int()'
# ^Built-in Functions 

#Library Functions 
- 'random'
- 'math'

import random
import math

#always put all imports first in the file 

print(math.pi)
#have to specify module name (could print from random.pi)
(modulename).(object/function)

import random

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
var = random.choice(mylist)
print(var)

#Inputs
#Inputs take a single str object and print it to the console to alert the user
#that a program is expecitng input

result = input('prompt')
#you must save the value in variable, otherwise it is immediately deleted
#You can call the variable anything you like as long as you follow the basic naming rules
var = input("please input a value:")
#Casting
#Input returns EVERYTHING as a str 
#you must cast in to an integer or float to use the object as a number type
#Shorter Form of Casting from input
var = int(input("pick a number:"))

