import turtle
import random

tos=turtle.Turtle()

def kare():
    mesafe=random.randrange(1,100)
    for i in range(4):
        tos.fd(mesafe)
        tos.right(90)

for i in range(36):
    xdeger=random.randrange(-300,300)
    ydeger=random.randrange(-300,300)
    kare()
    tos.pu()
    tos.goto(xdeger,ydeger)
    tos.pd()
