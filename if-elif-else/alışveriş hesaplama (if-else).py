# SORU 1

# Telefon ve tablet satışlarında toplam alışveriş miktarı 5000 tl üzeri
# ise bilgisayar satışlarında %20 indirim uygulayınız.Elde edilen toplam
# tutar 10.000 tl üzeri ise %18 KDV,10.000 tl altında ise %13 KDV uygulayıp
# son fiyatı detaylı bir şekilde yazdırınız.

telefonfiyat=int(input("Telefon adet fiyatını giriniz="))
tabletfiyat=int(input("Tablet adet fiyatını giriniz="))
bilgisayarfiyat=int(input("Bilgisayar adet fiyatını giriniz="))

telefonadet=int(input("Alınan telefon adedini giriniz="))
tabletadet=int(input("Alınan tablet adedini giriniz="))
bilgisayaradet=int(input("Alınan bilgisayar adedini giriniz="))

telefonborc=telefonfiyat*telefonadet
tabletborc=tabletfiyat*tabletadet
bilgisayarborc=bilgisayarfiyat*bilgisayaradet

toplamborc=telefonborc+tabletborc+bilgisayarborc
toplamborc1=telefonborc+tabletborc

if toplamborc1>5000 and toplamborc>10000:
    toplamborc=telefonborc+tabletborc+bilgisayarborc
    bilgisayarborc=bilgisayarborc-bilgisayarborc*0.20
    itoplamborc=telefonborc+tabletborc+bilgisayarborc
    kdv=itoplamborc*0.18
    toplam=itoplamborc+kdv
    print("Tebrikler bilgisayar kategorisinde geçerli %20 indirim kazandınız. ""Hesaplanan Tutar=",toplamborc,"tl. ""İndirimli Tutar=",itoplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam)
elif toplamborc1>5000 and toplamborc<10000:
    toplamborc=telefonborc+tabletborc+bilgisayarborc
    bilgisayarborc=bilgisayarborc-bilgisayarborc*0.20
    itoplamborc=telefonborc+tabletborc+bilgisayarborc
    kdv=itoplamborc*0.13
    toplam=itoplamborc+kdv
    print("Tebrikler bilgisayar kategorisinde geçerli %20 indirim kazandınız. ""Hesaplanan Tutar=",toplamborc,"tl. ""İndirimli Tutar=",itoplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam)
elif toplamborc>10000:
    toplamborc=telefonborc+tabletborc+bilgisayarborc
    kdv=toplamborc*0.18
    toplam=toplamborc+kdv
    print("Hesaplanantutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam,"tl.")
elif toplamborc<10000:
    toplamborc=telefonborc+tabletborc+bilgisayarborc
    kdv=toplamborc*0.13
    toplam=toplamborc+kdv
    print("Hesaplanantutar",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam,"tl.")







    
