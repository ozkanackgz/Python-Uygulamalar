aras=int(input("Ara sınav notunuzu giriniz="))
final=int(input("Final notunuzu giriniz="))
ort=(aras+final)/2
if ort>=90 and ort<=100:
    print("Harf notunuz A")
if ort>=80 and ort<90:
    print("Harf notunuz B")
if ort>=70 and ort<80:
    print("Harf notunuz C")
if ort>=50 and ort<70:
    print("Harf notunuz D")
if ort<50 and ort>=0:
    print("Harf notunuz E,dersten kaldınız.")
else:
    print("Ara sınav notunuzu yada final sınav notunuzu yanlış girdiniz.")

    
