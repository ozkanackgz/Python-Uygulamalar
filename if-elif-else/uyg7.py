# Kullanıcıdan girdiği iki sayı ve yapılacak işlem türü (toplama,çıkarma,
# çarpma,bölme)seçildiğinde,sonucu hesaplayarak ekranda gösteren programı
# yazdırınız.

sayibir=int(input("Birinci sayıyı giriniz: "))
sayiiki=int(input("İkinci sayiyi giriniz: "))
islem=int(input("Toplam için 1,çıkarma için 2 bölme için 3,çarpma için 4"))
sonuc=0

if islem==1:
    sonuc=sayibir+sayiiki
    print("Seçtiğiniz işlem toplama=",sayibir,"+",sayiiki,"=",sonuc)
elif islem==2:
    sonuc=sayibir-sayiiki
    print("Seçtiğiniz işlem çıkarma=",sayibir,"-",sayiiki,"=",sonuc)
elif islem==3:
    sonuc=sayibir/sayiiki
    print("Seçtiğiniz işlem bölme=",sayibir,"/",sayiiki,"=",sonuc)
elif islem==4:
    sonuc=sayibir*sayiiki
    print("Seçtiğiniz işlem çarpma=",sayibir,"*",sayiiki,"=",sonuc)
