import turtle
import random
import pygame
import math
window = turtle.Screen()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.shape("turtle")
turtle2.shape("turtle")
turtle1.color("blue")
turtle2.color("pink")
turtle1.penup()
turtle2.penup()
turtle1.speed(1)
turtle2.speed(1)
turtle1.goto(-100, 20)
turtle2.goto(-100, -20)
Distance = random.randrange(0, 100)
Distance2 = random.randrange(0, 100)
turtle1.forward(Distance)
turtle2.forward(Distance2)
turtle1.goto(-100, 20)
turtle2.goto(-100, -20)


for i in range(10):
    Distance3 = random.randrange(1, 10)
    Distance4 = random.randrange(1, 10)
    turtle1.forward(Distance3)
    turtle2.forward(Distance4)
turtle1.goto(-100, 20)
turtle2.goto(-100, -20)
window.exitonclick

pygame.init()
window = pygame.display.set_mode()
sidelength = 100
points = []
xpos = 100
ypos = 100
for x in range(5):
  points.clear()
  match x:
    case 0:
       num_sides = 3
    case 1:
       num_sides = 4
    case 2:
       num_sides = 6
    case 3:
       num_sides = 20
    case 4:
       num_sides = 100
    case 5:
       num_sides = 360
  for k in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * k)
    x = xpos + sidelength + math.cos(radians)
    y = ypos + sidelength + math.sin(radians)
    points.append((x,y))
  pygame.draw.polygon(window, "blue", points)
  pygame.display.flip()
  pygame.time.wait(2000)
  window.fill("white")
  pygame.display.flip()

