from tkinter import *
import time
from tkinter import messagebox
window=Tk()
window.geometry("300x250")
window.title("Universal Time Counter")
def submit():
    try:
        temp=int(hour.get())*3600+int(minute.get())*60+int(second.get())
    except:
        print("Please input the right value.")
    while temp>-1:
        mins,secs=divmod(temp,60)
        hours=00
        if mins>60:
            hours,mins=divmod(mins,60)
        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))
        window.update()
        time.sleep(1)
        if (temp==00):
            messagebox.showinfo("Time Countdown","Time's up!")
        temp-=1


    


hour=StringVar()
minute=StringVar()
second=StringVar()
hour.set("00")
minute.set("00")
second.set("00")
hourentry=Entry(window,width=3,font=("Helvetica",10,"normal"),textvariable=hour)
hourentry.place(x=80,y=20)
minuteentry=Entry(window,width=3,font=("Helvetica",10,"normal"),textvariable=minute)
minuteentry.place(x=130,y=20)
secondentry=Entry(window,width=3,font=("Helvetica",10,"normal"),textvariable=second)
secondentry.place(x=180,y=20)
button=Button(window,text="Set time countdown to",font=("Helvetica",10,"normal"),command=submit)
button.place(x=70,y=120)

mainloop()