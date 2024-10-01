# Bilgisayarın üretmiş olduğu 1-1000 arasındaki rastgele 100 sayının
# ortalamasını bulunuz.

import random

toplam=0
for i in range(100):
    sayi=random.randrange(1,5000)
    print(i,"ninci üretilen sayı=",sayi)
    toplam=toplam+sayi
    print("ara toplam=",toplam)
print("Bu sayıların ortalaması=",toplam/100)
