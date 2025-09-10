from tkinter import *
import random
window=Tk()
window.geometry("900x800")
tram=Frame(window)
tram.pack()
scoreimaad=0
scorecom=0
rpslist=["Rokc","Payper","Switzers"]
def computerwins():
    global scorecom, scoreimaad
    scorecom+=1
    lessgo.config(text="Computer/Bot wins!")
    scorecomputer.config(text=f"Computer Score: {scorecom}")
    scoreyou.config(text=f"Your Score: {scoreimaad}")
def nowins():
    global scorecom, scoreimaad
    scoreimaad+=1
    lessgo.config(text="You win!")
    scorecomputer.config(text=f"Computer Score: {scorecom}")
    scoreyou.config(text=f"Your Score: {scoreimaad}")
def tie():
    global scorecom, scoreimaad
    lessgo.config(text="Inconclusive! Haha!")
    scorecomputer.config(text=f"Computer Score: {scorecom}")
    scoreyou.config(text=f"Your Score: {scoreimaad}")
def mainfunct(player_input):
    computerinput=random.choice(rpslist)
    selectedcomputer.config(text=f"Computer Selected: {computerinput}")
    selectedhuman.config(text=f"You Selected: {player_input}")
    if player_input==computerinput:
        tie()
    elif player_input==rpslist[0] and computerinput==rpslist[1]:
        computerwins()
    elif player_input==rpslist[0] and computerinput==rpslist[2]:
        nowins()
    elif player_input==rpslist[1] and computerinput==rpslist[0]:
        nowins()
    elif player_input==rpslist[1] and computerinput==rpslist[2]:
        computerwins()
    elif player_input==rpslist[2] and computerinput==rpslist[0]:
        computerwins()
    elif player_input==rpslist[2] and computerinput==rpslist[1]:
        nowins()
ring_of_the_rock=Label(tram,text="Time to complete the ring of the rock with rock, paper, scissors!",font=("Arial",24,"normal"),fg="White",bg="grey")
lessgo=Label(tram,text="Let's start the game!",font=("Arial",50,"normal"),fg="White",bg="dark green")
ring_of_the_rock.pack(pady=10)
lessgo.pack(pady=10)
framet=Frame(window)
framet.pack()
opt=Label(framet,text="Your options:",font=("Arial",20,"normal"),fg="grey")
opt.grid(row=0,column=0)
reinforcedcrushedrock=Button(framet,text="Rokc",font=("Arial",20,"normal"),fg="Black",bg="red",command=lambda : mainfunct(rpslist[0]))
reinforcedcrushedrock.grid(row=0,column=1)
highqualityimaadpaper=Button(framet,text="Payper",font=("Arial",20,"normal"),fg="Black",bg="light grey",command=lambda : mainfunct(rpslist[1]))
highqualityimaadpaper.grid(row=0,column=2)
swiss_scissors=Button(framet,text="Switzers",font=("Arial",20,"normal"),fg="Black",bg="blue",command=lambda : mainfunct(rpslist[2]))
swiss_scissors.grid(row=0,column=3)
scoor=Label(framet,text="Score",font=("Arial",20,"normal"),fg="grey")
scoor.grid(row=1,column=0)
selectedhuman=Label(framet,text="You Selected:",font=("Arial",20,"normal"),fg="Black")
selectedcomputer=Label(framet,text="Computer Selected:",font=("Arial",20,"normal"),fg="Black")
scoreyou=Label(framet,text="Your Score:",font=("Arial",20,"normal"),fg="Black")
scorecomputer=Label(framet,text="Computer Score:",font=("Arial",20,"normal"),fg="Black")
selectedhuman.grid(row=1,column=0)
selectedcomputer.grid(row=2,column=0)
scoreyou.grid(row=3,column=0)
scorecomputer.grid(row=4,column=0)
mainloop()