from tkinter import *
import calendar
window1=Tk()
window1.geometry("450x450")
window1.title("Calendar - ImaadAppsAP")
def drawcal():
    window2=Tk()
    window2.title("ImaadCalendar")
    window2.geometry("550x600")
    year=int(entryyear.get())
    calcon=calendar.calendar(year)
    text=Text(window2,font="Consolas 10",wrap="none",height=60,width=80)
    text.insert("1.0",calcon)
    text.pack()
hehe_calendar=Button(window1,text="Welcome to ImaadCalendar! Better than yours!",font=("Helvetica",15,"bold italic"),fg="White",bg="Dark Green")
hehe_calendar.place(x=0,y=0)
yearh=Label(window1,text="Year:",font=("Sans Serif",20,"normal"))
yearh.place(x=200,y=80)
entryyear=Entry(window1,font=("Consolas 10",20,"normal"))
entryyear.place(x=80,y=120)
enter=Button(window1,text="Show Calendar",font=("Calibri",20,"italic"),command=drawcal)
enter.place(x=150,y=200)
exiteee=Button(window1,text="Exit",font=("Comic Sans",20,"normal"))
exiteee.place(x=190,y=300)


mainloop()