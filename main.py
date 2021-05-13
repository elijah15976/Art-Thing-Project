#Importing Stuff
import turtle
import time
import math
from core_functions import *

#Global Variables
side = 500
hypotenuse = math.sqrt((side**2)+(side**2))

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

#End of Program
time.sleep(5)