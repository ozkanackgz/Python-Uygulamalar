ilk=int(input("İlk terimi giriniz:"))
son=int(input("Son terimi giriniz:"))
art=int(input("Artış miktarını giriniz:"))

sonu=0
for i in range(ilk,son+1,art):
    sonuc=sonuc+i
print(sonuc)
