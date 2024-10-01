#Bir müşteri N adet ürün almıştır.Ürünlerin fiyatını girerek toplam borcunu
#öğrenmek istemektedir.Bu programı yazalım.

adet=int(input("Kaç ürün aldınız"))
toplam=0
sayac=0

for i in range(adet):
    i=int(input("ürün fiyatını giriniz"))
    sayac=sayac+1
    toplam=toplam+i
    print(sayac," adet ürünün ara toplam=",toplam)
