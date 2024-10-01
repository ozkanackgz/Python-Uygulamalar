import random

ad=str(input("Adınızı Giriniz="))
soyad=str(input("Soyadınızı Giriniz="))
gorev=str(input("Görevinizi Giriniz, M,İ,S ="))
cocuk=int(input("Çocuk Sayısını Giriniz="))
mesai=int(input("Mesai Sayısını Giriniz="))

prom=random.randrange(100,300)
hammaas=0
brutmaas=0
netmaas=0
gyazi=""
mesaikazanc=0
cocukkazanc=0

if gorev=="M":
    hammaas=15000
    gyazi="Firma Müdürü"
elif gorev=="İ":
    hammaas=9000
    gyazi="Firma İşçisi"
elif gorev=="S":
    hammaas=8000;
    gyazi="Sekreter"
    
brutmaas=hammaas+(cocuk*500)+prom

if mesai>30:
    brutmaas=brutmaas+(mesai*60)+(hammaas*0.05)
    mesaikazanc=(mesai*60)+(hammaas*0.05)
else:
    brutmaas=brutmaas+(mesai*60)
    mesaikazanc=(mesai*60)+(hammaas*0.05)

damgavergisi=brutmaas*0.005
brutmaas=brutmaas-(brutmaas*0.005)
gelirvergioran=0
cocukkazanc=cocuk*50

if brutmaas>10000 and brutmaas<=20000:
    netmaas=brutmaas-(brutmaas*0.15)
    gelirvergioran=15
elif brutmaas>20000 and brutmaas<=25000:
    netmaas=brutmaas-(brutmaas*0.20)
    gelirvergioran=20
elif brutmaas>25.000:
    netmaas=brutmaas-(brutmaas*0.25)
    gelirvergioran=25

print("Sayın:",ad," ",soyad)
print("Göreviniz:",gyazi)
print("Çocuk sayınız=",cocuk)
print("Bu aylık mesainiz=",mesai)
print("Promosyonunuz",prom)
print("Ham maaşınız=",hammaas)
print("Mesaiden kazancınız=",mesaikazanc)
print("Çocuk yardımı=",cocukkazanc)
print("Damga vergisi=",damgavergisi)
print("Gelir vergisi öncesi brüt maaş",brutmaas)
print("Gelir vergisi oranınız",gelirvergioran)
print("Net maaşınız",netmaas)
