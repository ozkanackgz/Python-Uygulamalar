# Klavyeden girilen belirli adet sayının en küçüğünü ve en büyüğünü bulan
# programı yazalım.

adet=int(input("Kaç sayı içerisinde en büyük ve en küçüğü bulacaksın="))
sayi=int(input("İlk sayıyı giriniz="))
eb=sayi
ek=sayi

for i in range(adet-1):
    say=int(input("Yeni sayıyı giriniz="))
    print("Girdiğiniz sayı=",say)
    if eb<say:
        eb=say
        print("Şimdiki en büyük sayı=",eb)
    if ek>say:
        ek=say
        print("Şimdiki en küçük sayı=",ek)
print(adet," adet sayı içerisinde en  büyük sayı=",eb,"en küçük sayı=",ek)
