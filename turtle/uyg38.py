import turtle
import random

ybs=turtle.Turtle()

renk=["blue","pink","red","yellow","gray","purple","green","black"]
ybs.pensize(3)
ybs.speed(13)

for i in range (36):
    rnum=random.randrange(1,7)
    ybs.left(10)
    ybs.circle(50)
    ybs.pencolor(renk[rnum])
