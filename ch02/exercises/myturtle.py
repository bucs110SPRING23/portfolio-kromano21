import turtle
window = turtle.Screen()
myturtle = turtle.Turtle()
colors = ["purple", "red"]
myturtle.shape('turtle')
for c in  colors:
  myturtle.color(c)
  myturtle.up()
  myturtle.forward(100)
  myturtle.down()
  for i in range(4):
        myturtle.left(90)
        myturtle.forward(50)
window.exitonclick()