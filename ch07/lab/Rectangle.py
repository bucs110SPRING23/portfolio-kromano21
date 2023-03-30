class Rectangle:
    def __init__(self, x, y, h, w):
        self.xcor = abs(x)
        self.ycor = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    def __str__(self):
        result = "(x:" + self.xcor + " y:" + self.ycor + ") " + "width:" + self.width + "height:" + self.height
        return result
