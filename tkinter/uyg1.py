from tkinter import*

ekran=Tk()
ekran.title("YBS-UYGULAMA")
ekran.geometry("500x500+700+150")


yazi=Label(text="Merhaba YBS")
yazi.place(x=30,y=20)

yazi2=Label(text="yazı acaba nerede YBS",fg="red",bg="yellow",font=("Arial","15","bold"))
yazi2.place(x=230,y=20)



def deneme():
    print("deneme")
    yazi["text"]=girdi.get()
    yazi["fg"]="red"
    yazi["font"]=("Arial","15","bold")
ilkbuton=Button(text="Yazı Yaz",command=deneme)
ilkbuton.place(x=100,y=200)
def bitir():
    quit()

kapat=Button(text="ÇIKIŞ",command=bitir)
kapat.place(x=100,y=240)

girdi=Entry()
girdi.place(x=30,y=100)


mainloop()
