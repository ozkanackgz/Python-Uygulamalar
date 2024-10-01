# SORU 3

# Bilgisayar satışlarında toplam tutar 6000 tl ve telefon satışlarında toplam
# tutar 3000 tl üzeri ise %10 indirim uygulayınız.Elde ettiğiniz son borç
# miktarına %25 KDV ekleyiniz.Son fiyatı detaylı bir şekilde yazdırınız.

bilgisayarfiyat=int(input("Bilgisayar adet fiyatını giriniz="))
telefonfiyat=int(input("Telefon adet fiyatını giriniz="))

bilgisayaradet=int(input("Alınan bilgisayar adedini giriniz="))
telefonadet=int(input("Alınan telefon adedini giriniz="))

bilgisayarborc=bilgisayarfiyat*bilgisayaradet
telefonborc=telefonfiyat*telefonadet
toplamborc=bilgisayarborc+telefonborc

if bilgisayarborc==6000 and telefonborc>3000:
    toplamborc=bilgisayarborc+telefonborc
    itoplamborc=toplamborc-toplamborc*0.10
    kdv=toplamborc*0.25
    toplam=itoplamborc+kdv
    print("Tebrikler %10 indirim kazandınız. ""Hesaplanan Tutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""İndirimli Tutar=",itoplamborc,"tl. ""TOPLAM=",toplam)
else:
    print("Hesaplanan Tutar=",toplamborc)


