
import turtle

ybs=turtle.Turtle()

for i in range(20):
    ybs.left(18)
    ybs.speed(10)
    ybs.begin_fill()
    for j in range (4):
        ybs.pencolor("blue")
        ybs.pensize(2)
        ybs.fd(20)
        ybs.right(90)
    ybs.color("yellow")
    ybs.end_fill()
    ybs.pu()
    ybs.fd(30)
    ybs.pd()
    ybs.begin_fill()
    for j in range (4):
        ybs.pencolor("red")
        ybs.pensize(2)
        ybs.fd(20)
        ybs.right(90)
    ybs.color("pink")
    ybs.end_fill()
    ybs.pu()
    ybs.fd(30)
    ybs.pd()
