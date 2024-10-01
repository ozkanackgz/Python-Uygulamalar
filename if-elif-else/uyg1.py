# Koşullu Durumlar

# Boolean İfadesi

# Bilgisayar bilimi temelde 0 ve 1 değerleri üzerine kurulmuştur;
# 0 değeri False(Yanlış),1 değeri True(Doğru) demektir.Bu ifadelere
# Boolean(Bool) ifadeleri denir.Doğru ve Yanlış değerleri korumak için
# kullanılan tipe bool adı verilmektedir.Sadece iki Boolean ifade
# değeri vardır:
# True(Doğru)(1)
# False(Yanlış)(0)


# Python'da İlişkisel Operatörler

# İfade             Anlamı
# x==y   Eğer x ve y birbirine eşitse(matematiksel olarak) doğrudur,değilse yanlıştır.
# x<y    Eğer x,y'den küçükse doğrudur;değilse yanlıştır.
# x<=y   Eğer x,y'den küçük ya da eşitse doğrudur;değilse yanlıştır.
# x>y    Eğer x,y'den büyükse doğrudur; değilse yanlıştır.
# x>=y   Eğer x,y'den büyük ya da eşitse doğrudur;değilse yanlıştır.
# x!=y   Eğer x,y'den farklı ise(büyük ya da küçük) doğrudur;değilse yanlıştır.


# Örnek:Bir kişinin bir dersten aldığı notu klavyeden girerek eğer 50 den
#       büyük ise geçtiniz,küçük ise kaldınız sonucunu veren programı yazınız.

ogrnot=int(input("Notunuzu giriniz="))
if ogrnot>50:
   print("Geçtiniz.")
else:
   print("Kaldınız.")







