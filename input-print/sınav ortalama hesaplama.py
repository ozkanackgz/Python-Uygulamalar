ad=input("Adınızı giriniz=")
soyad=input("Soyadınızı giriniz=")
vize=int(input("Vize notunuzu giriniz="))
ödev=int(input("Ödev notunuzu giriniz="))
final=int(input("Final notunuzu giriniz="))
ortalama=vize*0.30+ödev*0.20+final*0.50
print("Sayın;",ad,soyad,"Ortalamanız=",ortalama)
