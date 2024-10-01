import turtle
import random

tos=turtle.Turtle()

def kare():
    mesafe=random.randrange(1,100)
    for i in range(4):
        tos.fd(mesafe)
        tos.right(90)

for i in range(36):
    kare()
    tos.right(10)
