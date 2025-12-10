from tkinter import *

def additem():
    item=newitem_entry.get()
    if item:
        listy.insert("end",item)
        newitem_entry.delete(0,"end")
def deleter():
    #getting the index of all the selected items as tuples
    selectedindixes=listy.curselection()
    #print(selectedindixes)
    for i in selectedindixes:
        #print(i)
        listy.delete(i)
def graspandcontrol():
    #getting all the items of a listbox as a list
    allitems=listy.get(0,"end")
    print(allitems)
window=Tk()
#window.geometry("900x800")
window.title("Welcome to the histbox. Touch it, and you'll either get scratched and injured by a hostile cat or get $25 billion.")
scrollout=Scrollbar(window)
scrollout.pack(side=RIGHT,fill=Y)

listy=Listbox(window,height=10,width=60,selectmode="multiple",fg="white",bg="brown",yscrollcommand=scrollout.set)
listy.insert(1,"Flying Broomstick - features a cannon and 6 AIM-7 missiles!")
listy.insert(2,"Flee Powder, sends you to a random place and the people living there have to flee from you!")
listy.insert(3,"The B-Jet - powered from 10 Firebolt Broomsticks, flies 920 Km/h with 80 passengers!")
listy.insert(4,"Malicious Mountain, grows from a tiny mound to a mountain and anyone who goes on it is turned into a chicken!")
listy.insert(5,"Fat Aircraft")
listy.insert(6,"Howler or GET OUT siren")
listy.insert(7,"Harness the power of a entity with the Imaadshah")
listy.insert(8,"yummy delicious hot cross bun")
listy.insert(9,"what")
listy.insert(10,"why")
listy.insert(11,"when")
listy.insert(12,"how")
listy.insert(13,"imaad")
listy.insert(14,"welcome to the hissbox")
listy.pack()
scrollout.config(command=listy.yview)

newitem_entry=Entry(window,font=("Helvetica",20,"normal"))
newitem_entry.pack(pady=10)

buttons_frame=Frame(window)
buttons_frame.pack()

add_button=Button(buttons_frame,text="Add Item",font=("Helvetica",20,"normal"),command=additem)
add_button.grid(row=1,column=1)

del_button=Button(buttons_frame,text="Delete Item",font=("Helvetica",20,"normal"),command=deleter)
del_button.grid(row=1,column=2)

get_button=Button(buttons_frame,text="Get All Items",font=("Helvetica",20,"normal"),command=graspandcontrol)
get_button.grid(row=1,column=3)

clr_button=Button(buttons_frame,text="Clear Selection",font=("Helvetica",20,"normal"))
clr_button.grid(row=1,column=4)

mainloop()