#1.36


def drawSpiral(myTurtle1, myTurtle2, maxSide):
    for sideLength in range (1,maxSide+1,5):
        myTurtle1.forward(sideLength)
        myTurtle2.forward(sideLength)
        myTurtle1.right(140)
        myTurtle2.left(140)


import turtle
pg1=turtle.Turtle()
pg2=turtle.Turtle()
drawSpiral(pg1,pg2,100)

