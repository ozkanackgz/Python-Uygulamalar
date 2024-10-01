# Bilgisayarın üretmiş olduğu 0-100 arasındaki rastgele 20 sayının toplamını
# ve bu sayılardan en büyüğünü bulan ve ekrana yazdıran programı yazdırınız.

# 1-Random kütüphanesi ekle
# 2-For döngüsüyle 20 tane sayı üretmem gerekiyor
# Toplam değişkenini oluştur,üretilen her sayıyı toplama ekle en büyük
# değişkeni oluştur,üretilen her sayıyı en büyük değişkeniyle karşılaştır,
# eğer büyükse en büyük sayı yeni üretilen sayıdır.


import random
toplam=0
eb=0
for i in range(20):
    sayi=random.randrange(1,100)
    if sayi>eb:
        eb=sayi
        print("Şu anki en büyük sayı",eb)
    toplam=toplam+sayi
    print("üretilen=",sayi)
    print("ara toplam=",toplam)
