from tkinter import *
import speech_recognition as sr

def recog_voice():
    recogniser = sr.Recognizer()
    #setting microphone source for sound
    with sr.Microphone() as source:
        notepad.delete(1.0,END) #cleaning the previous content of the notepad
        notepad.insert(END,"Listening...")

        try:
            audio = recogniser.listen(source)
            text = recogniser.recognise_google(audio)
            notepad.delete(1.0,END)
            notepad.insert(END,text)
        except:
            notepad.delete(1.0,END)
            notepad.insert(END,"Uh oh you can't see anyhting except for this!")



window=Tk()
window.geometry("600x600")
window.title("Voice Notepad")
window.config(bg="dark green")

title=Label(window,text="Voice Notepad",font=("Helvetica",60,"bold"),fg="white",bg="Dark green")
title.place(x=20,y=30)
clickmeforfreecandy=Button(window,text="Click on me to start recording!",font=("Helvetica",20,"italic"),bg="white",fg="dark green",command=recog_voice)
clickmeforfreecandy.place(x=120,y=140)
notepad=Text(window,height=10,width=69)
notepad.place(x=20,y=240)
savethetext=Button(window,text="Save the Text",font=("Helvetica",20,"bold italic"),bg="white",fg="dark green")
savethetext.place(x=200,y=480)

mainloop()