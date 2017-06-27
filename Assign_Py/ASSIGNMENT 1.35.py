#ASSIGNMENT 1.35

def drawSpiral (myTurtle, maxSide):
    for sideLength in range (1,maxSide+1,5):
        myTurtle.forward(sideLength)
        myTurtle.right(sideLength)

import turtle

pagong=turtle.Turtle()
drawSpiral(pagong,100)
