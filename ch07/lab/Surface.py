from Rectangle import Rectangle
class Surface:
    def __init__(Self, filename, x, y, h, w):
        Self.rect = Rectangle(x, y, h, w)
        Self.image = filename
    def getRect(Self):
        return Self.rect
