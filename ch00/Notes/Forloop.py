import turtle
wn = turtle.Screen()
wn.bgcolor('green')
donatello = turtle.Turtle()
colors = ["purple", "red"]
donatello.shape('turtle')
for c in  colors:
  donatello.color(c)
  donatello.up()
  donatello.forward(100)
  donatello.down()
  for i in range(4):
        donatello.left(90)
        donatello.forward(50)
wn.exitonclick()
