import turtle


renk=["yellow","blue","pink","red","green",]
tos=turtle.Turtle()

tos.pensize(6)
for i in range(5):
    tos.pencolor(renk[i])
    tos.fd(200)
    tos.left(144)
