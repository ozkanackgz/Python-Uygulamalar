import turtle
screen=turtle.Screen()
tos=turtle.Turtle()
screen.setup(620,620)
screen.bgcolor("yellow")
renk=["red","green","blue","yellow","purple"]
tos.pensize(4)
tos.penup()
tos.pencolor("red")
m=0
for i in range(12):
    m=m+1
    tos.penup()
    tos.setheading(-30*i+60)
    tos.forward(150)
    tos.pendown()
    tos.forward(25)
    tos.penup
    tos.forward(20)
    tos.write(str(m),align="center",font=("Arial",12,"normal"))
    if m==12:
        m=0
    tos.home()
tos.home()
tos.setpos(0,-250)
tos.pendown()
tos.pensize(10)
tos.circle(250)
tos.penup()
tos.setpos(150,-270)
tos.pendown()
tos.pencolor("black")
tos.write("merhaba ybs",font=("Arial",12,"normal"))
tos.ht()
tos.pencolor("blue")
