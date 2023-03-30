class Rectangle:
    def __init__(self, x, y, h, w):
        self.xcor = abs(x)
        self.ycor = abs(y)
        self.height = abs(h)
        self.width = abs(w)
        return self.xcor, self.ycor, self.height, self.width
    def __str__(self):
        return "x:", self.xcor, self.ycor, 
    