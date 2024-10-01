# Bir öğrencinin ara sınav ve final notları %50 etkilemektedir.Öğrencinin
# ortalaması 0-45 arasında ise F,45-60 arasında ise "D" 60-70 arasında ise
# "C" 70-85 arasında ise B,85-100 arasında "A" notunu verdiren programı yazalım.

vize=int(input("Vize notunu giriniz="))
final=int(input("Final notunu giriniz="))
notort=(vize+final)/2

# if kullanıldığında tüm koşullar kontrol edilir.

if notort>=0 and notort<45:
    print("Ortalamanız=",notort," Harf notunuz:","F")
if notort>=45 and notort<60:
    print("Ortalamınız=",notort," Harf notunuz:","D")
if notort>=60 and notort<70:
    print("Ortalamanız=",notort," Harf notunuz:","C")
if notort>=70 and notort<85:
    print("Ortalamanız=",notort," Harf notunuz:","B")
if notort>=85 and notort<100:
    print("Ortalamanız=",notort," Harf notunuz:","A")

# elif kullanıldığında koşul sağlandıktan sonra diğer satırlar koşturulmaz.

if notort>=0 and notort<45:
    print("Ortalamanız=",notort," Harf notunuz:","F")
elif notort>=45 and notort<60:
    print("Ortalamınız=",notort," Harf notunuz:","D")
elif notort>=60 and notort<70:
    print("Ortalamanız=",notort," Harf notunuz:","C")
elif notort>=70 and notort<85:
    print("Ortalamanız=",notort," Harf notunuz:","B")
elif notort>=85 and notort<100:
    print("Ortalamanız=",notort," Harf notunuz:","A")
    
