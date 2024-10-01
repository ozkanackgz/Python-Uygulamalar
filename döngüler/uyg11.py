# 2000 ile 3500 sayıları arasında hem 7 ye,hemde 5 e bölünen sayıları
# sayıları ekrana yazdıralım ve bu sayıların toplamını ekrana yazdıralım.

top=0
for i in range(2000,3500):
    if i%7==0 and i%5==0:
        print(i)
        top=top+i
print("Toplam=",top)
