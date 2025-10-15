from tkinter import *
window=Tk()
window.geometry("400x400")
window.title("Introduction to Radio Buttons!")
la=Label(window,text="Make a choice.",font=("Arial",20,"normal"))
la.pack()

rgbvar=StringVar()
redrb=Radiobutton(window,text="Red",variable=rgbvar,value="Red")
redrb.pack()
greenrb=Radiobutton(window,text="Green",variable=rgbvar,value="Green")
greenrb.pack()
bluerb=Radiobutton(window,text="Red",variable=rgbvar,value="Blue")
bluerb.pack()

mainloop()