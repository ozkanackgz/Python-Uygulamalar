from tkinter import*

ekran=Tk()
ekran.title("YBS-UYGULAMA")
ekran.geometry("500x500+700+150")

w=Canvas(ekran,
         width=200,
         height=200)
w.pack()

points=[0,0,200,100,0,200]
w.create_polygon(points,outline="green",fill="yellow",width=5)
mainloop()
