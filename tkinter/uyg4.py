from tkinter import*

ekran=Tk()
ekran.title("YBS-UYGULAMA")
ekran.geometry("500x500+700+150")

def paint(event):
    x1,y1 =(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    w.create_oval(x1,y1,x2,y2,fill="yellow")
ekran=Tk()
w=Canvas(ekran,
         width=500,
         height=250)
w.pack(expand=YES,fill=BOTH)
w.bind("<B1-MOTİON>",paint)
mainloop()
