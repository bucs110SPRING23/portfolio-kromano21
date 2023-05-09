import turtle
sides = int(input("Enter the Number of Sides:"))
length = int(input("Enter the length of each side:"))
George = turtle.Turtle()
George.shape('turtle')
George.color("orange")
window = turtle.Screen()
Angle = (360/sides)
for i in range(sides):
    turtle.forward(length)
    turtle.left(Angle)
window.exitonclick()