from tkinter import*

ekran=Tk()
ekran.title("YBS-UYGULAMA")
ekran.geometry("500x500+700+150")


cizgi = Canvas(ekran,
               width=300,
               height=300)
cizgi.place(x=100,y=100)

cizgi.create_line(0,30,50,30, fill="#476042")
cizgi2 = Canvas(ekran,
               width=300,
               height=300)
cizgi2.place(x=100,y=200)

cizgi2.create_line(0,30,50,30, fill="#476042")

mainloop()

            
