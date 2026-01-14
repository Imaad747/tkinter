from tkinter import *
import pyttsx3

#intialising pyttsx3 engine 
engine = pyttsx3.init()

def s_p_e_a_k():
    t_e_x_t = entext.get()
    engine.say(t_e_x_t) #convert text to speech
    engine.runAndWait() #wait until speech is finished



window=Tk()
window.geometry("800x900")

bigbillboard = Label(window,text = "Text to Speech",font = ("Helvetica",85,"bold"),bg = "Red",fg = "White")
bigbillboard.place(x=0,y=0)
entext = Entry(bg = "Red",font = ("Helvetica",20,"bold"),fg = "White")
entext.place(x=260,y=440)
submitt = Button(window,text = "Submit",font = ("Helvetica",20,"bold"),command = s_p_e_a_k)
submitt.place(x=340,y=720)

mainloop()