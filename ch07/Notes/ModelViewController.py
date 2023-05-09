#Model-View-Controller is a general design pattern used for GUI programming
#Design Patterns are language agnostic abstractions of software patterns. 
#They are like blueprints for building stable and maintainable software components
#The MVC pattern is designed around 3 types of classes:
#Controller: class-type designed for managing application components
#Model: class-type designed to manage data
#Views: class-type to display the visuals 

#The controller handles all events and state changes, may or may not be the result of an event
#The View handles the display
#the Model handles the data

#Any moving or interactive element on screen is a widget. Widget must be represented by a class within the program 

#Models
#A class that maintains data for widgets is called a model
#Model Classes also implement the logic for working with that data
#Models are normal classes, it's just about how we use the class
#Let's say we've written a program to turn on and off individual LEDs in an array of LEDs
#The LED model will contain the data and alogrithms to turn an LED on or off
#The controller(the main() in the program below) notifies the correct LED object to toggle on or off when clicked 
#Notice, you will create multiple LED objects from 1 class
