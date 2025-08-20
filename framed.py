from tkinter import *
window=Tk()
window.geometry("900x800")
window.title("Order Papers for ImaadGoods - best store in the world")
f1=Frame(window)
f1.place(x=0,y=0,width=900,height=400)
f2oo=Frame(window,height=200)
f2oo.pack(side=BOTTOM,fill=X)
LebqBrickToys=Button(f1,text="Lebq Brick Minifigure + Castle",font=("Times New Roman",20,"italic"),fg="Red",bg="White")
LebqBrickToys.place(x=0,y=80)
flyingskateboard=Button(f1,text="Here is a flying rc aircaft. A child can fly in it! 100% Safe and easy to use!",font=("Arial",10,"bold"),fg="White",bg="Dark Green")
flyingskateboard.place(x=0,y=160)
realflyingbroomstick=Button(f1,text="Here is a flying broomstick, with a CFM56 jet engine on the back! It is easy to manuever by using the blast buttons on the sides!",font=("Helvetica",10,"bold italic"),fg="Yellow",bg="White")
realflyingbroomstick.place(x=0,y=240)
icecreep=Button(f2oo,text="You may enjoy Ice cream, but look again, because we have the Ice Creep! It creeps your enemies and makes you invincible. It'll surely never turn on you!",font=("Comic Sans",7,"normal"))
icecreep.grid(row=0,column=0)
magicwand=Button(f2oo,text="Here's an amazing magical wand! It has been stolen from hogwarts and has been mass produced! Buy a guide before buying this, it ain't so safe!",font=("Handel Gothic",7,"normal"))
magicwand.grid(row=1,column=0)
surveyortimetravel=Button(f2oo,text="For those who wish to see the past. Anywhere. Anytime. Spectate the earth. It's like Google Earth Timelapse but it is much more detailed and provides a deeper more useful insight into the past! Photos from 1960 and beyond! Also, we've stole some magic from hogwarts, so you can literally go there. Back in time!",font=("Helvetica",4,"bold"))
surveyortimetravel.grid(row=2,column=0)




mainloop()