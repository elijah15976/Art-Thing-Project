def polygon(tut, side, len, lr):
  for i in range(side):
    tut.forward(len)
    if lr == "left":
      tut.left(360/side)
    elif lr == "right":
      tut.right(360/side)

def jump(tut, x, y):
  tut.penup()
  tut.goto(x, y)
  tut.pendown()

def rect(tut, l, w, lr):
  for i in range(2):
    tut.forward(l)
    if lr == "left":
      tut.left(90)
    elif lr == "right":
      tut.right(90)
    tut.forward(w)
    if lr == "left":
      tut.left(90)
    elif lr == "right":
      tut.right(90)