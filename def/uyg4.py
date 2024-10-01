import turtle

tos=turtle.Turtle()

def kare(mesafe):
    for i in range(4):
        tos.fd(mesafe)
        tos.right(90)

for i in range(36):
    kare(100)
    tos.speed(0)
    tos.right(10)
