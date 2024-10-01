# Bir şirkette online alışveriş sistemi vardır.Sistemde pantolon,etek,gömlek
# ve çorap satılmaktadır.İşveren şöyle bir kampanya yapmak istiyor:

# 1-Eğer müşteri pantolon kategorisinde 500 tl üzeri alışveriş yapmışsa,
#  bu müşteriye gömlek alışverişlerinde %30 indirim uygulayıp detaylı son
#  borcunu yazdırınız.

# 2-Eğer müşteri toplamda 2000 tl lik alışveriş yapmışsa yada çorap ve etek
#  kategorisinde toplam 400 tl lik alışveriş yapmışsa toplam borca %19 indirim
#  uygulayınız.Borcu yazdırınız.

# 3-Eğer müşterinin toplam borcu 1000 tl ve pantolon reyonundan 300 tl alışveriş
#  yapmışsa %30 indirim,toplam borcu 1000 tl ve etek reyonunda toplamda 500 tl
#  alışveriş yapmışsa %40 indirim,toplam borcu 1000 tl ve çorap reyonunda
#  toplamda 400 tl alışveriş yapmışsa %47 indirimi toplam borç üzerinde yapınız
#  ve ekrana yazdırınız.Bir koşul sağlanadığında diğer indirimlerden
#  yararlanılamayacaktır.Müşteri lehine olacak şekilde programı yazınız.

# 4-Bir işletmedeki işyeri sahibi 2500 tl toplam alışveriş yapan müşterilerinin
#  harcamaları;
#
#  a.Etek harcamaları 500 tl üzeri ve pantolon harcamaları 1000 tl altı ise %10
#  b.Gömlek harcamaları 1200 tl üzeri yada çorap harcamaları 2000 üzeri ise %15
#  c.Etek ve gömlek harcamaları toplamı 1300 üzeri ve pantolon harcaması 2000 tl
#    ise %17 indirim uygulayınız.


pfiyat=int(input("Pantolonun fiyatını giriniz="))
padet=int(input("Pantolon adedini giriniz="))

efiyat=int(input("Eteğin fiyatını giriniz="))
eadet=int(input("Eteğin adedini giriniz="))

gfiyat=int(input("Gömleğin fiyatını giriniz="))
gadet=int(input("Gömleğin adedini giriniz="))

cfiyat=int(input("Çorap fiyatını giriniz="))
cadet=int(input("Çorap adedini giriniz="))

pborc=pfiyat*padet
eborc=efiyat*eadet
gborc=gfiyat*gadet
cborc=cfiyat*cadet
toplamborc=pborc+eborc+gborc+cborc
ecborc=eborc+cborc

#1
if pborc>500:
    gborc=gborc-(gborc*30/100)
    toplamborc=pborc+eborc+gborc+cborc
    print(toplamborc)
else:
    toplamborc=pborc+eborc+gborc+cborc
    print(toplamborc)

#2
if toplamborc>200 or ecborc>400:
    toplamborc=toplamborc-(toplamborc*19/100)
    print(toplamborc)
else:
    print(toplamborc)

#3
if toplamborc>1000 and cborc>400:
    toplamborc=toplamborc-(toplamborc*47/100)
    print(toplamborc)
elif toplamborc>1000 and eborc>500:
    toplamborc=toplamborc-(toplamborc*40/100)
    print(toplamborc)
elif toplamborc>1000 and pborc>300:
    toplamborc=toplamborc-(toplamborc*30/100)
    print(toplamborc)

#4
if toplamborc>2500:
    if eborc>500 and pborc<1000:
        toplamborc=toplamborc-(toplamborc*10/100)
        print(toplamborc)
    elif gborc>1200 or cborc>2000:
        toplamborc=toplamborc-(toplamborc*15/100)
        print(toplamborc)
    elif egborc>1300 and pborc<2000:
        toplamborc=toplamborc-(toplamborc*17/100)
        print(toplamborc)
    

    
    
    

