
import turtle
import random

tos=turtle.Turtle()

def cokgen(kenar,buyuk):
    for i in range(kenar):
        tos.fd(buyuk)
        aci=360/kenar
        tos.right(aci)
    tos.pu()
    xdeger=random.randrange(-400,400)
    ydeger=random.randrange(-400,400)
    tos.goto(xdeger,ydeger)
    tos.pd()

for i in range(100):
    tos.speed(10)
    kenar=random.randrange(3,30)
    buyuk=random.randrange(10,80)
    cokgen(kenar,buyuk)
