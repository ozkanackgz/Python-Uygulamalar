
import turtle

ybs=turtle.Turtle()

for i in range(20):
    ybs.left(18)
    ybs.speed(1)
    for j in range (4):
        ybs.pencolor("blue")
        ybs.pensize(2)
        ybs.fd(30)
        ybs.right(90)
    ybs.pu()
    ybs.fd(40)
    ybs.pd()
