# Çokgen olurşturma fonksiyonunu yazalım.

import turtle

tos=turtle.Turtle()

def cokgen(kenar,buyuk):
    for i in range(kenar):
        tos.fd(buyuk)
        aci=360/kenar
        tos.right(aci)

cokgen(20,100)
