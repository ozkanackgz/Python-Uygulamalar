# 30 adet kareden oluşan bir daire çizmek istiyorum.

import turtle

tosbik=turtle.Turtle()

for i in range(30):
    for i in range(4):
        tosbik.fd(30)
        tosbik.left(90)
    tosbik.left(12)
    tosbik.fd(40)
    
