# Muhammet hoca: Siz internet alışverişi yaparken arka planda sepetinizi
#                hesaplayan kodları yazıyoruz şuan.

# Bir manavda elma ve armut satılmaktadır.Elmanın kilosu 10 tl,armutun kilosu
# 8 tl dir.Elma ve armut alacak bir müşterinin kaç kg elma ve armut aldığını 
# sisteme girerek borcunu bulunuz.Eğer toplam borcu 100 tl üzerinde ise %10
# indirim uygulayınız.Ödemesi gereken miktarı ekrana yazdırınız.

# Algoritma:

# 1-Başla
# 2-Elma al.
# 3-Armut al.
# 4-Toplam borcu hesapla--->
# 4.1 Toplam borç 100 tl üzerinde ise %10 indirim uygula.
# 4.2 Toplam borç 100 tl altında toplam borcu uygula.
# 5-Bitir

elmakg=int(input("Kaç kg elma aldığınızı giriniz ="))
armutkg=int(input("Kaç kg armut aldığınızı giriniz ="))
borc=(10*elmakg)+(8*armutkg)
ödeme=0
if borc>=100:
    ödeme=borc-borc*0.10
    print("%10 indirim kazandınız. ""Normal fiyat =",borc,"tl. ""İndirimli fiyat =",ödeme,"tl.")
else:
    ödeme=borc
    print("Ödenecek tutar =",ödeme,"tl.")
    
