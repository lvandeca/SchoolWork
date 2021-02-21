'''
Turtle Graphics in Python
CIS 210 Project 2-3 Draw Flower

Author: Luke Vandecasteele

Credits: class notes and textbook

Using the built in function 'turtle' to
draw a flower
'''

from turtle import *

def main():
    drawFlower(25)
    return None

def drawFlower(numSquares):
    change_square_angle = 360/numSquares
    speed(0)
    color("green")
    pensize(4)
    ht()
    penup()
    setposition(0,-75)
    pendown()
    rt(-90)
    fd(75)
    color("red")
    pensize(1)
    for stuff in range(numSquares):
        drawPolygon(25,4)
        rt(change_square_angle)
    return None

def drawPolygon(sideLength,numSides):
    for item in range(numSides):
        rotate_angle = 360/numSides
        fd(sideLength)
        rt(rotate_angle)    
    return None

main()

