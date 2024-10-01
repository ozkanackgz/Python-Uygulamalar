# Klavyeden iki ürünün fiyatı girildiğinde toplam fiyat 200-300 tl arasında ise,
# %15 indirim, 300-400 tl arasında ise %22 indirim, 400-750 tl arasında ise
# %27 indirim, 750-1000 tl arasında ise %34 indirim, 1000 tl den fazla ise %40
# indirim uygulayıp kişinin borcunu ekrana detaylı olarak yazdırınız.



ürün1=int(input("1. ürünün fiyatını giriniz="))
ürün2=int(input("2. ürünün fiyatını giriniz="))
toplam=ürün1+ürün2
borc=0

if toplam>=200 and toplam<300:
    borc=toplam-(toplam*0.15)
    print("Hesaplanan tutar=",toplam,"tl. ""Tebrikler %15 indirim kazandınız.")
    print("İndirimli tutar=",borc,"tl.")
elif toplam>=300 and toplam<400:
    borc=toplam-(toplam*0.22)
    print("Hesaplanan tutar=",toplam,"tl. ""Tebrikler %22 indirim kazandınız.")
    print("İndirimli tutar=",borc,"tl.")
elif toplam>=400 and toplam<750:
    borc=toplam-(toplam*0.27)
    print("Hesaplanan tutar=",toplam,"tl. ""Tebrikler %27 indirim kazandınız.")
    print("İndirimli tutar=",borc,"tl.")
elif toplam>=750 and toplam<1000:
    borc=toplam-(toplam*0.34)
    print("Hesaplanan tutar=",toplam,"tl. ""Tebrikler %34 indirim kazandınız.")
    print("İndirimli tutar=",borc,"tl.")
elif toplam>=1000:
    borc=toplam-(toplam*0.40)
    print("Hesaplanan tutar=",toplam,"tl. ""Tebrikler %22 indirim kazandınız.")
    print("İndirimli tutar=",borc,"tl.")
