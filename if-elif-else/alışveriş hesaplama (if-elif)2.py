# SORU 4c

# Bilgisayar parçaları satan bir dükkanda ekran kartı kategorisinde alınan
# ekrantı değeri veya alınan ekran kartları toplam maliyeti 14.000 tl ve üzeri
# ise alınacak klavye veya oyuncu kulaklıklarında %50 indirim uygulanacaktır.
# Laptoplarda ise alınan ürünlerin maliyeti 12.000 tl ve üzeri ise alınacak
# monitörlerde %18 indirim uygulanacaktır.Toplam tutar 30.000 tl ve üzerinde
# ise %12 KDV 30.000 tl altında ise %8 KDV uygulanacaktır.Bu algoritmayı
# kodlayınız.

ekrankfiyat=int(input("Ekran kartı adet fiyatını giriniz="))
klavyefiyat=int(input("Klavye adet fiyatını giriniz="))
oyuncklkfiyat=int(input("Oyuncu kulaklığı adet fiyatını giriniz="))
laptopfiyat=int(input("Laptop adet fiyatını giriniz="))
monitorfiyat=int(input("Monitör adet fiyatını giriniz="))

ekrankadet=int(input("Alınan ekran kartı adedini giriniz="))
klavyeadet=int(input("Alınan klavye adedini giriniz="))
oyuncklkadet=int(input("Alınan oyuncu kulaklığı adedini giriniz="))
laptopadet=int(input("Alınan laptop adedini giriniz="))
monitoradet=int(input("Alınan monitör adedini giriniz="))

ekrankborc=ekrankfiyat*ekrankadet
klavyeborc=klavyefiyat*klavyeadet
oyuncklkborc=oyuncklkfiyat*oyunculklkadet
laptopborc=laptopfiyat*laptopadet
monitorborc=monitorfiyat*monitoradet

toplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc

if ekrankborc>=14000 and toplamborc>=30000:
    toplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    klavyeborc=klavyeborc-klavyeborc*0.50
    oyuncklkborc=oyuncuklk-oyuncklk*0.50
    itoplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    kdv=itoplamborc*0.12
    toplam=itoplamborc+kdv
    print("Tebrikler klavye ve oyuncu kulaklıklarında geçerli %50 indirim kazandınız. ""Hesaplanan Tutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""İndirimli Tutar=",itoplamborc,"tl. ""TOPLAM=",toplam,"tl. ")
elif ekrankborc>=14000 and toplamborc<=30000:
    toplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    klavyeborc=klavyeborc-klavyeborc*0.50
    oyuncklkborc=oyuncuklk-oyuncklk*0.50
    itoplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    kdv=itoplamborc*0.8
    toplam=itoplamborc+kdv
    print("Tebrikler klavye ve oyuncu kulaklıklarında geçerli %50 indirim kazandınız. ""Hesaplanan Tutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""İndirimli Tutar=",itoplamborc,"tl. ""TOPLAM=",toplam,"tl. ")
elif laptopborc>=12000 and toplamborc>=30000:
    toplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    monitorborc=monitorborc-monitorborc*0.18
    itoplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    kdv=itoplamborc*0.12
    toplam=itoplamborc+kdv
    print("Tebrikler monitörlerde geçerli %18 indirim kazandınız. ""Hesaplanan Tutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""İndirimli Tutar=",itoplamborc,"tl. ""TOPLAM=",toplam,"tl. ")
elif laptopborc>=12000 and toplamborc<=30000:
    toplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    monitorborc=monitorborc-monitorborc*0.18
    itoplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    kdv=itoplamborc*0.8
    toplam=itoplamborc+kdv
    print("Tebrikler monitörlerde geçerli %18 indirim kazandınız. ""Hesaplanan Tutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""İndirimli Tutar=",itoplamborc,"tl. ""TOPLAM=",toplam,"tl. ")
elif toplamborc>=30000:
    toplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    kdv=toplamborc*0.12
    toplam=toplamborc+kdv
    print("Hesaplanan Tutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam,"tl. ")
elif toplamborc<=30000:
    toplamborc=ekrankborc+klavyeborc+oyuncklkborc+laptopborc+monitorborc
    kdv=toplamborc*0.8
    toplam=toplamborc+kdv
    print("Hesaplanan Tutar=",toplamborc,"tl. ""KDV Tutarı=",kdv,"tl. ""TOPLAM=",toplam,"tl. ")

    
