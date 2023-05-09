import turtle
import random
window = turtle.Screen()
turtle.screensize(600, 600)
turtle1 = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(0)
xpos = turtle.xcor()
ypos = turtle.ycor()
if 600 >= abs(xpos):
        is_in_screen = True
elif abs(600) >= ypos:
        is_in_screen = True
elif abs(xpos) > 600:
        is_in_screen = False
elif abs(ypos) > 600:
        is_in_screen = False
while is_in_screen == True:
    value = random.randrange(0, 2)
    if value == 1:
        turtle.right(90)
        turtle.forward(50)
    if value ==0:
        turtle.left(90)
        turtle.forward(50)