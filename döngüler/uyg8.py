# Verilen bir mesajı istenen sayıda ekrana yazdıran programı yazalım.

mesaj=input("mesajınızı giriniz:")
adet=int(input("mesajınız kaç kere ekranda yazdırılsın?="))

for i in range(adet):
    print(mesaj)
