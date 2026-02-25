from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
window=Tk()
window.title("School Book")
window.config(bg="Dark green")
myaddressbook={}
def edit():
    clearall()
    index=contacts_list.curselection()
    if index:
        name.insert(0,contacts_list.get(index))
        details=myaddressbook[name.get()]
        address.insert(0,details[0])
        numberphone.insert(0,details[1])
        email.insert(0,details[2])
        birthday.insert(0,details[3])
    else:
        messagebox.showinfo("Error","Select a name.")
def clearall():
    name.delete(0,END)
    address.delete(0,END)
    numberphone.delete(0,END)
    email.delete(0,END)
    birthday.delete(0,END)

def update():
    key=name.get()
    if key=="":
        messagebox.showinfo("Error","Name cannot be empty")
    else:
        if key not in myaddressbook.keys():
            contacts_list.insert(END,key)
            myaddressbook[key]=(address.get(),numberphone.get(),email.get(),birthday.get())
            clearall()

def delete():
    index=contacts_list.curselection()
    if index:
        del myaddressbook[contacts_list.get(index)]
        contacts_list.delete(index)
        clearall()
    else:
        messagebox.showinfo("Error","Select a name")

def openfile():
    global myaddressbook
    reset()
    file_in=askopenfile(title="open file")
    if file_in:
        myaddressbook=eval(file_in.read())
        for key in myaddressbook.keys():
            contacts_list.insert(END,key)
            bookname.configure(text=os.path.basename(file_in.name))
    else:
        messagebox.showinfo("Error 404","No Address Book Opened.")

def display(event):
    newwindow=Toplevel(window)
    index=contacts_list.curselection()
    contact=""
    if index:
        key=contacts_list.get(index)
        contact="Name: "+key+"\n\n"
        details=myaddressbook[key]
        contact+="Address: "+details[0]+"\n"
        contact+="Phone Number: "+details[1]+"\n"
        contact+="Email Address: "+details[2]+"\n"
        contact+="Birthday: "+details[3]+"\n"


    lbl=Label(newwindow)
    lbl.grid(row=0,column=0)
    lbl.configure(text=contact)

def reset():
    clearall()
    contacts_list.delete(0,END)
    myaddressbook.clear()
    bookname.configure(text="My Address Book")
def save():
    file_out=asksaveasfile(defaultextension=".txt")
    if file_out:
        print(myaddressbook,file=file_out)
        reset()
    else:
        messagebox.showinfo("Error 404","Address Book not saved.")





bookname=Label(window,text="My School Book",font=("Helvetica",20,"bold"),width=35,foreground="white",background="dark green")

bookname.grid(row=0,column=1,pady=10,columnspan=3)


openbutton=Button(window,text="Open")

openbutton.grid(row=0,column=3,pady=10)

contacts_list=Listbox(window,width=30,height=15)
contacts_list.grid(row=2,column=0,columnspan=3,rowspan=5)

name_label=Label(window,text="Name:",background="gold")
name_label.grid(row=2,column=3)

name=Entry(window)
name.grid(row=2,column=4,padx=5)


address_label=Label(window,text="Roll Number:",background="gold")
address_label.grid(row=3,column=3)

address=Entry(window)
address.grid(row=3,column=4,padx=5)


phone_number=Label(window,text="ID:",background="gold")
phone_number.grid(row=4,column=3)

numberphone=Entry(window)
numberphone.grid(row=4,column=4,padx=5)

email_label=Label(window,text="Grade:",background="gold")
email_label.grid(row=5,column=3)

email=Entry(window)
email.grid(row=5,column=4,padx=5)

birthday_label=Label(window,text="School Account:",background="gold")
birthday_label.grid(row=6,column=3)

birthday=Entry(window)
birthday.grid(row=6,column=4,padx=5)

edit_button=Button(window,text="Edit",width=10,command=edit)
edit_button.grid(row=7,column=0,padx=12,pady=12)

delete_button=Button(window,text="Delete",width=10,command=delete)
delete_button.grid(row=7,column=1,pady=12)

update_button=Button(window,text="Update/Add",width=12,command=update)
update_button.grid(row=7,column=4,pady=12)

save_button=Button(window,text="Save",width=10,command=save)
save_button.grid(row=8,column=1,pady=12)

clear_all=Button(window,text="Clear",width=12,command=clearall)
clear_all.grid(row=7,column=5,pady=12)






        








mainloop()




