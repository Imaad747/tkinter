from tkinter import *
from tkinter.ttk import *
window=Tk()
window.geometry("800x900")
window.title("The menu for BOAC (British Overseas Airways Corporation). Special South Asian Menu, September 1968")
def varprogre():
    widgee=Progressbar(window,orient=HORIZONTAL,length=100,mode="determinate")
    widgee.pack()
    import time
    widgee["value"]=20
    window.update_idletasks()
    time.sleep(1)
    widgee["value"]=40
    window.update_idletasks()
    time.sleep(1)
    widgee["value"]=60
    window.update_idletasks()
    time.sleep(1)
    widgee["value"]=80
    window.update_idletasks()
    time.sleep(1)
    widgee["value"]=100

menoobarge=Menu(window)
fightile=Menu(menoobarge,tearoff=0)
menoobarge.add_cascade(label="File",menu=fightile)
fightile.add_command(label="New File",command=None)
fightile.add_separator()
fightile.add_command(label="Delete",command=None)
fightile.add_separator()
fightile.add_command(label="Save",command=None)
fightile.add_command(label="SaveProgress",command=varprogre)
food_opt=Menu(menoobarge,tearoff=0)
menoobarge.add_cascade(label="Food",menu=food_opt)
food_opt.add_separator()
food_opt.add_command(label="Chicken 2 pack",command=None)
food_opt.add_separator()
food_opt.add_command(label="Lamb Mandi + Lamb",command=None)
food_opt.add_separator()
food_opt.add_command(label="Biriyani, chicken or lamb",command=None)
food_opt.add_separator()
food_opt.add_command(label="Masala?????????????",command=None)
food_opt.add_separator()
food_opt.add_command(label="Fried Chicken",command=None)
food_opt.add_separator
food_opt.add_command(label="Beef",command=None)
food_opt.add_separator()
food_opt.add_command(label="Seafood Full Package and Platter",command=None)






window.config(menu=menoobarge)
mainloop()
