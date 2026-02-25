from tkinter import *
import time
import random
from tkinter import messagebox

window=Tk()
window.title("Ping Pong")
window.resizable(0,0)

canvas_width=600
canvas_height=500
canvas=Canvas(window,width=canvas_width,height=canvas_height,bg="Black")
canvas.pack()

score_font=("Arial",20,"bold")

score_text=canvas.create_text(300,20,font=score_font,text="0:0",fill="Blue")
canvas.create_line(canvas_width/2,0,canvas_width/2,canvas_height,fill="White")

x=canvas_width/2
y=canvas_height/2
r=50

x0=x-r
y0=y-r
x1=x+r
y1=y+r

middle_circle=canvas.create_oval(x0,y0,x1,y1,outline="White")

paddle_width=20
paddle_height=80

class Paddle:
    def __init__ (self,canvas,color,x,y):
        self.canvas=canvas
        self.paddle=canvas.create_rectangle(x,y,x+paddle_width,y+paddle_width,fill=color)
        self.delta=0
    def moveupdownusing(self,keypressup,keypressdown):
        self.canvas.bind_all(keypressup,self.moveup)
        self.canvas.bind_all(keypressdown,self.movedown)
    def draw(self):
        self.canvas.move(self.paddle,0,self.delta)
        pos=self.canvas.coords(self.paddle)
        if pos[1]<=0:
            self.delta=0
        if pos[3]>=canvas_height:
            self.delta=0
    def moveup(self,event):
        self.delta=-4
    def movedown(self,event):
        self.delta=4


    

mainloop()