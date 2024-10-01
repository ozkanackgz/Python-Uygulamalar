# Bir mağazadan alınan ürünün fiyatı 100 tl üstünde ise kargo ücreti
# alınmamakta,100 tl altında ise 10 tl kargo ücreti alınmaktadır.Buna
# göre fiyatı girilen bir ürünün toplam maliyetini hesaplayan programı yazınız.

fiyat=int(input("Ürün fiyatını giriniz ="))
borc=0
if fiyat>=100:
    borc=fiyat
    print("Ödenecek tutar =",borc,"tl.")
else:
    borc=fiyat+10
    print("Ödenecek tutar =",borc,"tl. ""Kargo ücreti dahil edilmiştir.")
