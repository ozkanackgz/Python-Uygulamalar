import math

girdi=int(input("Hangi sayının faktöriyelini bulmak istersin:"))
sonuc=1
for i in range(girdi,0,-1):
    sonuc=sonuc*i
    print(i)
    print(sonuc)
