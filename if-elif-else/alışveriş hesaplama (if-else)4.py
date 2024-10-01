# SORU 4b

# Bir çiftlikte şişe süt satışlarında toplam tutar 7000 tl ve sepet yumurta 
# satışlarında toplam tutar 2000 tl üzeri ise sepet yumurta tutarı üzerinde  
# %7 indirim uygulanacaktır.Bu algoritmayı kodlayınız.

sütf=int(input("Şişe süt fiyatını giriniz="))
ymrtaf=int(input("Koli sepet fiyatını giriniz="))

sütadet=int(input("Alınan şişe süt adedini giriniz="))
ymrtaadet=int(input("Alınan sepet yumurta adedini giriniz="))

sütborc=sütf*sütadet
ymrtborc=ymrtaf*ymrtaadet

toplamborc=sütborc+ymrtborc

if sütborc==7000 and ymrtborc>2000:
    toplamborc=sütborc+ymrtborc
    ymrtborc=ymrtborc-ymrtborc*0.7
    itoplamborc=sütborc+ymrtborc
    print("Hesaplanan Tutar=",toplamborc,"tl. ""İndirimli Tutar=",itoplamborc,"tl.")
else:
    print("Hesaplanan Tutar=",toplamborc,"tl.")
    

