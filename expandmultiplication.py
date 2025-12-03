from tkinter import *

def multiplicatorplankton():
    numstore=int(thentrynumabsolute.get())
    multipliplankton=numvar.get()
    #print(type(numstore))
    #print(type(multipliplankton))
    #print(numstore*multipliplankton)
    for i in range(multipliplankton):
        output_row=f"{numstore} X {i} = {numstore*i}\n"
        script.insert(END,output_row)
        



window=Tk()
window.geometry("800x900")
window.title("Multiplication Generator")
    
title=Label(window,text="Multiplication Generator",font=("Helvetica",20,"bold italic"))
title.place(x=200,y=30)
numenterlab=Label(window,text="Number",font=("Helvetica",20))
numenterlab.place(x=30,y=100)
numvar=IntVar()
ten=Radiobutton(text="10",font=("Helvetica",20),variable=numvar,value=10)
twenty=Radiobutton(text="20",font=("Helvetica",20),variable=numvar,value=20)
thirty=Radiobutton(text="30",font=("Helvetica",20),variable=numvar,value=30)
ten.place(x=670,y=100)
twenty.place(x=670,y=150)
thirty.place(x=670,y=200)
thentrynumabsolute=Spinbox(window,from_=1,to=100,font=("Helvetica",20,"bold"))
thentrynumabsolute.place(x=200,y=100)
wattsthebutton=Button(window,text="Generate",font=("Helvetica",20,"italic"),command=multiplicatorplankton)
wattsthebutton.place(x=320,y=220)
script=Text(window,height=17,width=50,font=("Helvetica",20,"bold italic"))
script.place(x=20,y=320)

#nurmmulplankton=
mainloop()