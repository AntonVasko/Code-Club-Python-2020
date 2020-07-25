from turtle import *
from random import *

colormode(255)
def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)
  
def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown()
  
shape("turtle")
i = 0
while i<100:
    randomcolour()
    randomplace()
    stamp()
    i += 1
