#1 ile 1000 arasında bilgisayarın bulduğu rastgele 5 sayının toplamını
#ve ortalamasını bulalım.

#1-376
#2-456
#3-900
#4-45
#5-704

#rastgele bulduğum sayıları toplayıp 5 e böleceğiz.

import random
toplam=0
for i in range (5):
    i=random.randrange (1,1000)
    toplam=toplam+i
    print(i)
    print(toplam)
sonuc=toplam/5
print("ortalama=",sonuc)
