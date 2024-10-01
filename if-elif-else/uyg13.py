aras=int(input("Ara sınav notunuzu giriniz="))
if aras>100 or aras<0:
    print("0 ile 100 arasında bir not giriniz")
    aras=int(input("Ara sınav notunuzu tekrar giriniz."))
final=int(input("Final notunuzu giriniz="))
ort=(aras+final)/2
if ort>=90 and ort<=100:
    print("Harf notunuz A")
elif ort>=80 and ort<90:
    print("Harf notunuz B")
elif ort>=70 and ort<80:
    print("Harf notunuz C")
elif ort>=50 and ort<70:
    print("Harf notunuz D")
elif ort<50 and ort>=0:
    print("Harf notunuz E,dersten kaldınız.")
else:
    print("Ara sınav notunuzu yada final sınav notunuzu yanlış girdiniz.")

    
