#When the user interacts with a window, it causes an event
#In a GUI environemnt, when a user interacts with a window
#The operating system creates a data object to give a running program information on the user's actions

#Programs can run specific algorithms based on the type of event
#Connect Actions 
#1. Mouse Button Clicked
#2. Space Key Pressed
#to algorithms
#1. make a random color dot at a location on screen 
#2. Clear all dots from Screen

#Simon Says
import pygame
import random
pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "purple", "green", "blue"]
random.shuffle(colors)
for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(500)
    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(250)
message = """
Your Arrow Keys correspond to the following colors:
    Up: red
    Down: purple
    Left: Green
    Right: Blue

    Click on the window, enter the sequence, then press <enter> in the console
"""
input(message)

#User Events
#pygame.event.get() asks the OS to return a list of all events
#Important Concepts for Handling Events 
#1. You only need to respond to the events you care about 
#2. Each time you request events, it empties the event's list
#3. You only have one chance to respond to an event 

#Events Object
#Each event has a corresponding pygame object called an Event Object
#access with pygame.EVENT_NAME
#The event object has information about the event
#event.type: the kind of event
#event.key: the key associated with the event 
#You must always first check type, then the data of the event
#Event data depends on the type of event. For example, some event objects may have a key attribute and some may not 

#Event Loop - where you request and respond toe vents
#You should only be responding to events in one place at a time in your program
user_guess = []
for event in pygame.event.get():
  if event.type == pygame.KEYDOWN:
    if(event.key == pygame.K_UP):
      screen.fill("red")
      user_guess.append("red")
    elif(event.key == pygame.K_DOWN):
      screen.fill("purple")
      user_guess.append("purple")
    elif(event.key == pygame.K_LEFT):
      screen.fill("green")
      user_guess.append("green")
    elif(event.key == pygame.K_RIGHT):
      screen.fill("blue")
      user_guess.append("blue")
    pygame.display.flip()
    pygame.time.wait(1000)
print("You Entered:", user_guess)
print("The correct pattern was", colors)

if user_guess == colors:
      print("Correct! You win.")
else:
      print("Were you paying attention?")

pygame.quit()
#Remember - each time you request events, it empties the event queue
#If you do not respond to an event, it will not be available again   