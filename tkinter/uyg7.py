import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import*

ekran=Tk()

ekran.geometry("600x200+800+60")

sayilar=[1,2,3,4,5,6,7,8,9,10]
def hesap():
    sonuc=int(sayhep.get())*int(sayhep.get())
    kareyazi["text"]=sonuc
sayhep=ttk.Combobox()
sayhep['values']=sayilar
sayhep.current(0)
sayhep.place(x=100,y=100)

kareyazi=Label(text="Yazinin Karesi")
kareyazi.place(x=260,y=100)
yap=Button(text="HESAPLA",command=hesap)
yap.place(x=350,y=100)
mainloop()
