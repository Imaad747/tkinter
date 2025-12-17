from tkinter import *
from tkinter.filedialog import *


def addessay():
    data=inslistentree.get()
    if data:
        listbot.insert("end",data)
        inslistentree.delete(0,"end")
def deletedef():
    selectedwordpieces=listbot.curselection()
    for i in selectedwordpieces:
        listbot.delete(i)
def openfile():
    #this command will open the file dialog
    file_to_open=askopenfile(title="Open File")
    if file_to_open is not None:
        listbot.delete(0,END)    
        #reading the content of the file
        filedata=file_to_open.readlines()
        print(filedata)
        for data in filedata:
            listbot.insert(END,data.strip())
def savee():
    #getting the save dialog box with the default extension as .txt
    file_to_save=asksaveasfile(defaultextension=".txt")
    if file_to_save is not None:
        for item in listbot.get(0,END):
            print(item,file=file_to_save)
        listbot.delete(0,END)

        

window=Tk()
window.geometry("900x800")
open=Button(window,text="Open",font=("Helvetica",20),command=openfile)
open.place(x=20,y=50)
delete=Button(window,text="Delete",font=("Helvetica",20),command=deletedef)
delete.place(x=780,y=50)
save=Button(window,text="Save",font=("Helvetica",20),command=savee)
save.place(x=300,y=50)
add=Button(window,text="Add",font=("Helvetica",20),command=addessay)
add.place(x=580,y=50)
inslistentree=Entry(window,font=("Helvetica",20))
inslistentree.place(x=67,y=180)
listbot=Listbox(window,font=("Helvetica",20),width=52,height=9,selectmode="multiple")
listbot.place(x=67,y=300)

mainloop()