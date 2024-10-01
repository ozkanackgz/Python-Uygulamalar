#Bir markette elma 10 tl,armut 8 tl den satılmaktadır.Müşteriden kaç kilo elma ve armut
#aldığını isteyiniz.Eğer toplam borcu 100 tl ve üzeri ise %10 indirim,200-300 tl arası
#ise %20 indirim 300 tl den fazla ise %25 indirim yapıp son borcunu söyleyiniz.

elmakg=10
armutkg=8

elma=int(input("kaç kilo elma aldıgınızı giriniz:"))
armut=int(input("kaç kilo armut aldığınızı giriniz:"))

elmakilo=elmakg*elma
armutkilo=armutkg*armut

toplamborc=elmakilo+armutkilo

if toplamborc>=100 and toplamborc<=200:
    toplamborc=toplamborc-(toplamborc*10/100)
elif toplamborc>200 and toplamborc<=300:
     toplamborc=toplamborc-(toplamborc*20/100)
elif toplamborc>300:
     toplamborc=toplamborc-(toplamborc*25/100)
     print("Son borcunuz:",toplamborc,)
else:
     print("hiçbir indirim kazanamadınız. borcunuz:",toplamborc,)
