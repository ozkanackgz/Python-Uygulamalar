# Yarıçap değerleri 1 den 10 a kadar olan çemberlerin alanlarını
# ekrana yazdıran programı yazınız.


import math

for i in range(1,11):
    alan=math.pi*math.pow(i,2)
    print("yarıçapı ",i, "olan çemberin alanı=",math.ceil(alan))
