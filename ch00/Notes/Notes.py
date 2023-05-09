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

sides = int(sides)
#casting string to integer

#External Modules
#Website Py.Py
#Free to download, often use
pygame
pygame-Menu 
# Framework - collection of modules, large libraries. Bunch of stuff to use, not a program itself. 

#Top of the File
import pygame

pygame.init()
#sets everything up, use before doing anything with pygame 

screen = pygame.display.set_mode()
#left blank, full screen
#(300, 300) - 300 by 300 window
#screen: variable
#pygame: modules that contain modules are called frameworks
#display: Submodule of pygame
#set_mode: Function of the display submodule 

screen.fill("red")
pygame.time.wait(2000)
pygame.display.flip()
screen.fill("blue")
pygame.time.wait(2000)
pygame.display.flip()
screen.fill("green")
pygame.time.wait(2000)
pygame.display.flip()
#won't display until you tell it to 
#flip - less problems but could be laggier than pygame.display.update()
#ideally want to wait after you flip so you can view the color after changing the image
pygame.time
#pygame module for monitoring time 
pygame.draw
#pygame module for drawing 
pygame.draw.rect(screen, "pink",[10, 10, 100, 100])
#dimensions = [x, y, width, height]
pygame.display.flip()
pygame.time.wait(5000)
#in graphic programming, y is inverted (increases downward)
#negative coordinates are always offscreen
#can list dimesnsions such as 
dimensions = [10, 10, 20, 30]
#and then...
pygame.draw.rect(screen, "pink", dimensions)
#Exercise: drawing with pygame
screen_size = screen.get_size()
dimensions = [screen_size[0] / 2, screen_size[1] / 2, 250, 250]
random.randrange(1, 10)
#Generates Random Number from 1-9 (does not include the upper-limit value)

## Events
## Operating system handles events
## Your Program -> OS: Anything happens

##OS => event
##type of event == operation 
# - click 
# - key_presses

# connect actions to algorithms 
#Simon Says

import pygame
import random
pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(2000)

    message = """
       Simon says:
       UP: RED
       DOWN: BLUE
       LEFT: GREEN
       RIGHTL YELLOW

       click on the window, enter sequence, m then press enter
"""
response = input(message)

#pygame.EVENT_OBJECT

for event in pygame.event.get():
    print(event)

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
             screen.fill("red")
             user_sequence.append("red")
        elif event.key == pygame.K_DOWN:
             screen.fill("blue")
             user_sequence.append("blue")