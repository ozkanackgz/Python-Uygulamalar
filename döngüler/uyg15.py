# Aralığı kullanıcı tarafından girilen(ilk ve son değer) aralıktaki 5 ile
# bölünen sayıların adeti,7 ile bölünen sayıların adetinden kaç fazladır?

ilkdeger=int(input("aralığın ilk değerini giriniz="))
sondeger=int(input("aralığın son değerini giriniz="))
besadet=0
yediadet=0

for i in range(ilkdeger,sondeger):
    if i%5==0:
        besadet=besadet+1
    if i%7==0:
        yediadet=yediadet+1

print(besadet," tane 5 ile bölünebilen sayı vardır")
print(yediadet," tane 7 ile bölünebilen sayı vardır")
print("Farkları=",besadet-yediadet)
