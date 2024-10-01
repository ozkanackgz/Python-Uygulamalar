from tkinter import*

ekran=Tk()
ekran.title("YBS-UYGULAMA")
ekran.geometry("500x500+700+150")
def deger():
    toplam=w.get()+w2.get()
    al["text"]=toplam

w=Scale(ekran,from_=0,to=200)
w.place(x=100,y=100)
w2=Scale(ekran,from_=0,to=50,tickinterval=10,orient=HORIZONTAL)
w2.place(x=200,y=200)
al=Label(text="Sliderdaki degerler")
al.place(x=200,y=300)
yap=Button(ekran,text="Değer al ve göster",command=deger)
yap.place(x=200,y=400)

mainloop()
