import turtle

ybs=turtle.Turtle()

for i in range(120):
    ybs.speed(10)
    ybs.dot(8,"red")
    ybs.forward(20)
    ybs.right(3)
    print(ybs.pos())
