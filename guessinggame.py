from tkinter import *
import random
from tkinter import messagebox
window=Tk()
window.geometry("900x800")
window.title("Guessing names")
thesecretguardedbyitsimaad=random.randint(1,100)
def terriblegreetingswithdisrespect():
    entee=entryname.get()
    messagebox.showinfo(title=f"Hello {entee}. You'll need to gain the power of the red rocks.",message=f"I'm... thinking... of *hiccup* a number, {entee}! It ranges from 1 to 100, itsImaad told me so!")
welcometothewhat=Label(window,text="Welcome, salutations, hello, greetings to the lucky question box.",font=("Helvetica",22,"bold"),fg="white",bg="Dark Blue")
welcometothewhat.place(x=0,y=0)
whatsyourname=Label(window,text="What's your name?",font=("Helvetica",20,"bold"),fg="Black",bg="White")
whatsyourname.place(x=0,y=60)
entryname=Entry(window,font=("helvetica",20,"bold italic"),fg="White",bg="black")
entryname.place(x=370,y=60)
okayokay=Button(window,text="Ok",font=("helvetica",15,"normal"),fg="White",bg="Red",command=terriblegreetingswithdisrespect)
okayokay.place(x=770,y=60)
takeaguess=Label(window,text="Take a guess. You have to. It's why you're here!",font=("helvetica",12,"bold"),fg="White",bg="Orange")
takeaguess.place(x=0,y=120)
takeaguesssentry=Entry(window,font=("helvetica",15,"bold"),fg="Black",bg="White")
takeaguesssentry.place(x=400,y=120)
listenspaceguesslistenseekspace=Button(window,text="Guess?",font=("helvetica",10,"bold"),fg="White",bg="Green")
listenspaceguesslistenseekspace.place(x=770,y=120)

mainloop()
