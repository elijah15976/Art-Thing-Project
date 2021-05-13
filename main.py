#Importing Stuff
import turtle
import time
import math
from core_functions import *

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
polygon(bob, 4, 500, "right")
bob.end_fill()
bob.right(45)

#Insides
bob.forward(math.sqrt(500000))

#End of Program
time.sleep(5)