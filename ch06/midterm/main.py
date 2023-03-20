import turtle

def main():
    welcome()
    foundationbuilder(widthfinder(), heightfinder())

def welcome():
    """
    This function creates a welcome message for the user
    args: 
    return: None
    """
    welcomemessage = "Welcome to the Turtle Construction Company!" 
    print(welcomemessage)

def widthfinder():
    """
    This function acquires the width of the building from the user
    args:
    return: int
    """
    widthmessage = "Please indicate how wide you would like your building. Due to resource constraints, the turtle construction company can only build to a width of 600: "
    buildingwidth = int(input(widthmessage))
    return buildingwidth

def heightfinder():
    """
    This function acquires the height of the building from the user
    args:
    return: int
    """
    heightmessage = "Please indicate how tall you would like your building to be. Due to resource constraints, the turtle construction company can only build to a height of 600: "
    buildingheight = int(input(heightmessage))
    return buildingheight

def windowsetup():
    """
    This function sets up the turtle window
    args:
    return: object
    """
    window = turtle.Screen()
    screenx = 600
    screeny = 600
    window.screensize(screenx, screeny)
    return window

def turtlesetup():
    """
    This function sets up the turtle object and adjusts its shape and speed
    args: 
    return: object
    """
    turtlebuilder = turtle.Turtle()
    turtleshape = 'turtle'
    turtlebuilder.shape(turtleshape)
    turtlespeed = 1
    turtlebuilder.speed(turtlespeed)
    return turtlebuilder

def foundationbuilder(width=0, height=0):
    """
    This function draws the building
    args: int
    return: None
    """  
    window = windowsetup()
    turtlebuilder = turtlesetup()
    turtlecolor1 = "green"
    turtlebuilder.color(turtlecolor1)
    turtlebuilder.penup()
    xpos = -300
    ypos = -290
    turtlebuilder.setpos(xpos, ypos)
    turtlebuilder.pendown()
    floorlength = 600
    turtlebuilder.forward(floorlength)
    turtlebuilder.setpos(xpos, ypos)
    turtlecolor2 = "orange"
    turtlebuilder.color(turtlecolor2)
    angle = 90
    turtlebuilder.left(angle)
    turtlebuilder.forward(height)
    turtlebuilder.right(angle)
    turtlebuilder.forward(width)
    turtlebuilder.right(angle)
    turtlebuilder.forward(height)

main()