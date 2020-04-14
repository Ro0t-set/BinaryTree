from tkinter import *
from math import *
from colour import Color
import random

finestra = Tk()
finestra.geometry("600x600")
finestra.title("BoaringProject")
canvas = Canvas(finestra, width= 650, height= 600, bg="black")
canvas.pack()
red = Color("green")
colors = list(red.range_to(Color("violet"), 10000))
color= 0


def genera_albero(cavanas, x1, y1, x2, y2, node, angleX,angleY, leng):
    if node ==0:
        return 0
    global color
    
    width =  (y2/100)
    color = color+1
    linea = cavanas.create_line(x1, y1, x2, y2, fill=colors[color], width= width)

    finestra.update()
    
    ramoX = leng * cos(angleX)
    ramoY = leng  * abs(sin(angleY))

    genera_albero(cavanas, x2, y2, (x2 + ramoX) , (y2 - ramoY- 10), node-1, angleX - 0.97,  angleY -0.17, leng*0.83)
    genera_albero(cavanas, x2, y2, (x2 - ramoX) , (y2 - ramoY- 5), node-1, -angleX- 0.17, - angleY+ 0.47, leng*0.83)

genera_albero(canvas, 325, 600, 325, 450, 13, 0.5, 1, 70)
finestra.mainloop()
