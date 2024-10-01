# SORU 4a

# Mobilya eşyaları satan bir mağazada toplam tutarı 17000 tl ve üzeri olan  
# koltuk takımı alışverişinde televizyon üniteleri alışverişinde %15 indirim
# uygulanacaktır.Toplam tutar 28000 tl ve üzeri ise %8 KDV tutarı altında ise
# %6 KDV tutarı uygulanacaktır.Bu algoritmayı kodlayınız.

koltuktfiyat=int(input("Koltuk takımı fiyatını giriniz="))
televizyonüfiyat=int(input("Televizyon ünite fiyatını giriniz="))

koltuktadet=int(input("Alınan koltuk takımı adetini giriniz="))
televizyonüfiyat=int(input("Alınan televizyonü adetini giriniz="))

koltuktborc=koltuktfiyat*koltuktadet
televizyonüborc=televizyonüfiyat*televizyonüadet

toplamborc=koltuktborc+televizyonüborc

if koltuktborc>=17000 and toplamborc>=28000: 
    toplamborc=koltuktborc+televizyonüborc
    televizyonüborc=televizyonüborc-televizyonü*0.15
    itoplamborc=koltuktborc+televizyonüborc
    kdv=itoplamborc*0.8
    toplam=itoplamborc+kdv
    print("Tebrikler televizyon ünitelerinde geçerli %15 indirim kazandınız. ""Hesaplanan Tutar=",toplamborc,"tl. ""İndirimli Tutar=",itoplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam)
elif koltuktborc>=17000 and toplamborc<=28000: 
    toplamborc=koltuktborc+televizyonüborc
    televizyonüborc=televizyonüborc-televizyonü*0.15
    itoplamborc=koltuktborc+televizyonüborc
    kdv=itoplamborc*0.6
    toplam=itoplamborc+kdv
    print("Tebrikler televizyon ünitelerinde geçerli %15 indirim kazandınız. ""Hesaplanan Tutar=",toplamborc,"tl. ""İndirimli Tutar=",itoplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam)
elif toplamborc>=28000:
    toplamborc=koltuktborc+televizyonüborc
    kdv=toplamborc*0.8
    toplam=toplamborc+kdv
    print("Hesaplanan Tutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam,"tl.")
elif toplamborc<=28000:
    toplamborc=koltuktborc+televizyonüborc
    kdv=toplamborc*0.6
    toplam=toplamborc+kdv
    print("Hesaplanan Tutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam,"tl.")
else:
    print("Hesaplanan Tutar=",toplamborc,"tl.")



