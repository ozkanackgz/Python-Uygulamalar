#1 den 1000 e kadar olan sayıları büyüktür küçüktür komutları ile 20 tahminde
#bulmaya çalışan programı yazınız.

import random
sayi=random.randrange(1,1000)
hak=0
for i in range(20):
    tahmin=int(input("tahmini giriniz"))
    hak=hak+1
    print("kullandığım hak=",hak)
    if tahmin==sayi:
        print("Tebrikler oyunu kazandınız")
    elif tahmin>sayi:
        print("Daha küçük bir sayı giriniz")
    elif tahmin<sayi:
        print("daha büyük sayı giriniz")
    
