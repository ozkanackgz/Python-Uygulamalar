# Klavyeden girilen bir sayının faktöriyelini bulan programı yazınız.

sayi=int(input("Faktöriyelini bulmak istediğiniz sayıyı giriniz="))
carpim=1
for i in range(sayi,0,-1):
    print(i)
    carpim=carpim*i
    print(carpim)
