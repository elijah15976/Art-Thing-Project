#Importing Stuff
import turtle
import time
import math
from core_functions import *

#Global Variables
side = 500
hypotenuse = math.sqrt((side**2)+(side**2))

smaller_Side = math.sqrt(((side/2)**2)+((side/2)**2))
smaller_Hypotenuse = math.sqrt((smaller_Side**2)+(smaller_Side**2))

#Background
turtle.bgcolor("light blue")

#Turtle
bob = turtle.Turtle()
bob.speed(0)

#Start Position
jump(bob, 0, 350)
bob.right(45)

#Sideways Square
bob.color("black")
bob.fillcolor("white")
bob.begin_fill()
polygon(bob, 4, side, "right")
bob.end_fill()
bob.right(45)

#Corner To Corner
bob.forward(hypotenuse)
bob.right(135)
bob.penup()
bob.forward(side)
bob.right(135)
bob.pendown()
bob.forward(hypotenuse)
bob.right(135)
bob.penup()

#Side To Side
bob.forward(side/2)
bob.right(90)
bob.pendown()
bob.forward(side)
bob.right(135)
bob.penup()
bob.forward(math.sqrt(((side/2)**2)+((side/2)**2)))
bob.right(135)
bob.pendown()
bob.forward(side)

#Inner Sqaure
bob.right(135)
polygon(bob, 4, math.sqrt(((side/2)**2)+((side/2)**2)), "right")
bob.penup()

#Inner Square Side To Side
bob.fillcolor("orange")
bob.forward(smaller_Side/2)
bob.right(45)
bob.begin_fill()
bob.pendown()
polygon(bob, 4, smaller_Hypotenuse/2, "right")
bob.end_fill()

#End of Program
bob.color("orange")
jump(bob, 0, 0)
time.sleep(5)