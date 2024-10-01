import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import*
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import*

ekran=Tk()

ekran.geometry("600x800+800+60")

kdvliste=[1,8,18,30]
karliste=[5,10,20,50,100]
urunler=["TELEFON","BİLGİSAYAR","TELEVİZYON"]

ufiyat=Label(text="Ürünün Fiyatı:")
ufiyat.place(x=10,y=20)

fgir=Entry()
fgir.place(x=150,y=20)

ucesit=Label(text="Ürünün Çeşidi")
ucesit.place(x=230,y=20)
ukdv=Label(text="Ürünün KDVsi:")
ukdv.place(x=10,y=60)
def ata(event):
    if urunlerkombo.get()=="TELEFON":
        karkombo['values']=telefonkar
    if urunlerkombo.get()=="BİLGİSAYAR":
        karkombo['values']=bilgkar
    if urunlerkombo.get()=="TELEVİZYON":
        karkombo['values']=televkar
    

urunlerkombo=ttk.Combobox()
kurunlerkombo['values']=urunler
urunlerkombo.bind('<<ComboboxSelected>>',ata)
urunlerkombo.current(0)
urunlerkombo.place(x=350,y=20)

kdvkombo=ttk.combobox()
kdvkombo['values']=kdvliste
kdvkombo.current(0)
kdvkombo.place(x=150,y=60)

ukar=Label(text="Ürünün Karı:")
ukar.place(x=10,y=100)

karkombo=ttk.combobox()
karkombo['values']=karliste
karkombo.current(0)
karkombo.place(x=150,y=100)

skar=Label(text="Ürünün satış fiyatı")
skar.place(x=90,y=140)

def hesap():
    karlifiyat=int(fgir.get())+(int(fgir.get())*int(karkombo.get())/100)
    kdvlifiyat=karlifiyat+(karlifiyat*int(kdvkombo.get())/100)
    print(karlifiyat)
    print(kdvlifiyat)

yap=Button(text="HESAPLA",command=hesap)
yap.place(x=90,y=180)
mainloop()
