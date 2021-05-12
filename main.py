import turtle
import time
from core_functions import *

turtle.bgcolor("light blue")

bob = turtle.Turtle()

bob.speed(0)

jump(bob, 0, 350)
bob.right(45)

bob.color("white")
bob.begin_fill()
polygon(bob, 4,500, "right")
bob.end_fill()

#End of Program
time.sleep(5)