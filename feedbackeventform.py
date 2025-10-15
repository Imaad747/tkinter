from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("800x900")
window.title("Event Feedback Form")
def submit_details():
    getthefeed=feedback_text.get("1.0","end")
    listindex=randomizer.curselection()
    infolisters=randomizer.get(listindex[0])
    excelexcel=excel.get()
    if excelexcel:
        excelexcel="Rated As Excellent"
    gooood=goodvariesalot.get()
    if gooood:
        gooood="Rated As Good"
    iwsbdvar=itwasstablebutdull.get()
    if iwsbdvar:
        iwsbdvar="Rated As Average"
    belowexpectations=disappointment.get()
    if belowexpectations:
        belowexpectations="Rated As Poor, overall terrible"
    iknowyourage=agedrumroll.get()
    print(excelexcel)
    print(gooood)
    print(iwsbdvar)
    print(belowexpectations)
    print(iknowyourage)
    print(getthefeed)
    print(infolisters)
    messagebox.showinfo("Thank you for your feedback!",f"{excelexcel},{gooood},{iwsbdvar},{belowexpectations},{iknowyourage},{getthefeed},{infolisters}")
    

    


title_label=Label(window,text="Please enter your feedback!",font=("Helvetica",30,"normal"),bg="red",fg="white")
title_label.place(x=150,y=30)
feedback_text=Text(window,font=("Times New Roman",20,"normal"),width=50,height=5)
feedback_text.place(x=30,y=100)
randomizer=Listbox(window,height=10,width=60,font=("Times New Roman",20,"normal"),fg="white",bg="Red")
randomizer.insert(1,"Workshop")
randomizer.insert(2,"Talk")
randomizer.insert(3,"Networking")
randomizer.place(x=0,y=300)
excel=BooleanVar()
excellent=Checkbutton(window,text="Excellent",variable=excel,bg="White",fg="Dark Green")
excellent.place(x=30,y=650)
goodvariesalot=BooleanVar()
somechocolategoodies=Checkbutton(window,text="Good",variable=goodvariesalot,bg="white",fg="Brown")
somechocolategoodies.place(x=260,y=650)
itwasstablebutdull=BooleanVar()
itsalrightbut=Checkbutton(window,text="Average",variable=itwasstablebutdull,bg="white",fg="grey")
itsalrightbut.place(x=460,y=650)
disappointment=BooleanVar()
unacceptableexperience=Checkbutton(window,text="Poor",variable=disappointment,bg="white",fg="dark blue")
unacceptableexperience.place(x=720,y=650)
agedrumroll=Spinbox(window,from_=18,to=60)
agedrumroll.place(x=30,y=707)
theintercontinentalsummit=Button(window,text="Submit",font=("Helvetica",20,"normal"),fg="white",bg="Green",command=submit_details)
theintercontinentalsummit.place(x=320,y=787)
mainloop()