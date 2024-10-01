import random
sayi=random.randrange(1,100)
tahmin=int(input("Sayıyı tahmin ediniz="))
if tahmin==sayi:
    print("Tebrikler bildiniz.")
elif tahmin>sayi:
    print("Daha düşük bir sayı giriniz.")
    tahmin=int(input("Sayıyı tahmin ediniz="))
elif tahmin<sayi:
    print("Daha büyük bir sayı giriniz.")
    tahmin=int(input("Sayıyı tahmin ediniz="))



    
