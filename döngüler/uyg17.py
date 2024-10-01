#Kullanıcının belirlemiş olduğu aralıktaki sayıların,artış miktarı belirlenerek
#toplamını bulan programı yazalım.

ilk=int(input("İlk terimi giriniz:"))
son=int(input("Son terimi giriniz:"))
art=int(input("Artış miktarını giriniz:"))
sonuc=((son+ilk)*(son-ilk+art))/(2*art)
print(sonuc)
