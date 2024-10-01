# İlk ve son değeri verilen aralıktaki sayıların toplamını bulunuz,ilk ve
# son değeri kullanıcı belirlesin.

ilkdeger=int(input("Başlangıç değerini giriniz="))
sondeger=int(input("Son değeri giriniz="))
top=0

for i in range(ilkdeger,sondeger):
    top=top+i
print("Belirttiğiniz aralıktaki sayıların toplamı=",top)
