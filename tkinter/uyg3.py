from tkinter import*

ekran=Tk()
ekran.title("YBS-UYGULAMA")
ekran.geometry("500x500+700+150")

w = Canvas(ekran,  width=300, height=300)
w.place(x=100,y=200)
w.create_rectangle(50,20,130,80, fill="#476042")

mainloop()
