import turtle

trtl = turtle.Turtle()
# trtl.forward(100)
# trtl.left(45)
# trtl.forward(100)
# trtl.right(90)
# trtl.forward(100)
trtl.color('blue','yellow')# the first is outline color and the second is the fill color
trtl.begin_fill()
trtl.forward(100)
trtl.left(90)
trtl.forward(100)
trtl.left(90)
trtl.forward(100)
trtl.left(90)
trtl.forward(100)
trtl.end_fill()

trtl.penup() # space between the 2 square
trtl.forward(100)
trtl.pendown()

trtl.color('blue','yellow')# the first is outline color and the second is the fill color
trtl.begin_fill()
trtl.forward(100)
trtl.left(90)
trtl.forward(100)
trtl.left(90)
trtl.forward(100)
trtl.left(90)
trtl.forward(100)
trtl.end_fill()




turtle.done()
