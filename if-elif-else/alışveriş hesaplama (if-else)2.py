# SORU 2

# Telefon,tablet ve bilgisayar satışlarında toplam borç miktarı 10.000 tl
# üzeri ise yada telefon ve bilgisayar satışlarında toplam miktar 5000 tl
# üzeri ise %23 indirim uygulayınız.Son fiyatı detaylı bir şekilde yazdırınız.

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
toplamborc1=telefonborc+bilgisayarborc

if toplamborc>10000 or toplamborc1>5000:
    toplamborc=telefonborc+tabletborc+bilgisayarborc
    itoplamborc=toplamborc-toplamborc*0.23
    print("Tebrikler %23 indirim kazandınız. ""Hesaplanan tutar=",toplamborc,"tl. ""İndirimli Tutar=",itoplamborc,"tl.")
else:
    print("Hesaplanan Tutar=",toplamborc)
    


    
