from tkinter import*

ekran=Tk()
ekran.title("YBS-UYGULAMA")
ekran.geometry("500x500+700+150")


sayibir=Label(text="birinci sayı:")
sayibir.place(x=30,y=20)

girdibir=Entry()
girdibir.place(x=130,y=20)

sayiiki=Label(text="ikinci sayı:")
sayiiki.place(x=30,y=50)

girdiiki=Entry()
girdiiki.place(x=130,y=50)

sonuc=sayibir=Label(text="SONUÇ=")
sonuc.place(x=130,y=70)

def topla():
    print("Toplama işlemi")
    islem=int(girdibir.get())+int(girdiiki.get())
    print(islem)
    sonuc["text"]=int(girdibir.get()),"+",int(girdiiki.get()),"=",islem
toplama=Button(text="+",command=topla)
toplama.place(x=90,y=100)

def cikar():
    print("Çıkarma işlemi")
    islem=int(girdibir.get())-int(girdiiki.get())
    print(islem)
    sonuc["text"]=int(girdibir.get()),"-",int(girdiiki.get()),"=",islem
cikarma=Button(text="-",command=cikar)
cikarma.place(x=130,y=100)

def carp():
    print("Çarpma işlemi")
    islem=int(girdibir.get())*int(girdiiki.get())
    print(islem)
    sonuc["text"]=int(girdibir.get()),"x",int(girdiiki.get()),"=",islem
carpma=Button(text="x",command=carp)
carpma.place(x=170,y=100)

def al():
    print("Factorial alma işlemi")
    import math
    islem=print(math.factorial(int(girdibir.get())))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"!","=",islem
alma=Button(text="!",command=al)
alma.place(x=210,y=100)





