from tkinter import *
from time import strftime
window=Tk()
window.geometry("800x200")
def timetickets():
    timetransporter=strftime("%d %B %Y, %I:%M:%S %p, %Z")
    timelab.config(text=timetransporter)
    timelab.after(1000,timetickets)

window.title("Click Clock Click Clock time is on, on the run!")
timelab=Label(window,font=("Helvetica",22,"normal"),fg="White",bg="Dark Green")

timelab.pack()
timetickets()
mainloop()