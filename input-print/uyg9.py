# 4-Mağaza 3 al 2 öde kampanyası düzenlemektedir.Her bir kategoride
#   (pantolon,etek,gömlek ve çorap) alınan her 3 ürünün bir tanesi bedavaya
#  gelmektedir.Bir müşterinin almış olduğu ürünler sonucunda toplam borcunu
#  hesaplayınız.

pNumber=int(input("Alınan pantolon adedini giriniz="))
pPrice=int(input("Pantolonun adet fiyatını giriniz="))
s1=pNumber//3
bP1=(pNumber-s1)*pPrice
eNumber=int(input("Alınan etek adedini giriniz="))
ePrice=int(input("Eteğin adet fiyatını giriniz="))
s2=eNumber//3
bP2=(eNumber-s2)*ePrice
gNumber=int(input("Alınan gömlek adedini giriniz="))
gPrice=int(input("Gömleğin adet fiyatını giriniz="))
s3=gNumber//3
bP3=(gNumber-s3)*gPrice
cNumber=int(input("Alınan çorap adedini giriniz="))
cPrice=int(input("Çorabın adet fiyatını giriniz="))
s4=gNumber//3
bP4=(cNumber-s4)*cPrice
bigPrice=bP1+bP2+bP3+bP4
print("Hesaplanan tutar=""",bigPrice,"tl.")
