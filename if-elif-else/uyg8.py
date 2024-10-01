# Klavyeden iki ürünün fiyatı girildiğinde toplam fiyat 200 tl'den fazla ise,
# 2. üründen %25 indirim yaparak ödenecek tutarı gösteren uygulamayı yapalım.

urunbir=int(input("1. ürünün fiyatını giriniz="))
uruniki=int(input("2. ürünün fiyatını giriniz="))
toplam=urunbir+uruniki

if toplam>200:
    toplam=urunbir+(uruniki-(uruniki*25/100))
    print("İkinci üründe %25 indirim kazandınız ödemeniz gereken=",toplam)
else:
    print("İndirim kazanamadınız borcunuz=",toplam,"tl.")
