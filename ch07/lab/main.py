from Rectangle import Rectangle
from Surface import Surface

r = Rectangle(10, 10, 10, 10)
assert((r.xcor, r.ycor, r.height, r.width) == (10,10,10,10))
r = Rectangle(-1, 1, 1, 1)
assert((r.xcor, r.ycor, r.height, r.width) == (1,1,1,1))
r = Rectangle(1, -5, 1, 1)
assert((r.xcor, r.ycor, r.height, r.width) == (1,5,1,1))
r = Rectangle(1, 1, -10, 1)
assert((r.xcor, r.ycor, r.height, r.width) == (1,1,10,1))
r = Rectangle(1, 1, 1, -1000)
assert((r.xcor, r.ycor, r.height, r.width) == (1,1,1,1000))

s = Surface("myimage.png", 10, 10, 10, 10)
assert((s.rect.xcor, s.rect.ycor, s.rect.height, s.rect.width) == (10,10,10,10))
srect = s.getRect()
assert((srect.xcor,  s.getRect().ycor, srect.height,  srect.width) == (10,10,10,10))
assert s.image
print("Test Complete!")
