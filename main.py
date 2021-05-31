from tkinter import *
from math import *
from colour import Color
import random
import math
import time

finestra = Tk()
finestra.geometry("600x600")
finestra.title("BoaringProject")
canvas = Canvas(finestra, width= 600, height= 600, bg="black")
canvas.pack()
green = Color("green")

color= 0

prob = 6 # prob to generate recursive: 0 => 0%, 10 => 100%
length = 30.0 # length of first line
nMax = 40 # max recursive level

colors = list(green.range_to('violet', nMax + 1))

def binary_prob_tree(x1, y1, level):
    nRand = random.randint(1, 10)

    if nRand > prob or level > nMax:
        return 0
    
    partial_length = length - level * 0.8

    x2_p1 = x1 - 1/2*length
    y2_p1 = y1 - 1/2*length

    x2_p2 = x1 + 1/2*length
    y2_p2 = y1 - 1/2*length
    
    """
    create 2 new smaller lines, on direction top left and top right 
    from the given x1 and x2
    """
    canvas.create_line(x1, y1, x2_p1, y2_p1, fill=colors[level], width= 3)
    canvas.create_line(x1, y1, x2_p2, y2_p2, fill=colors[level], width= 3)

    finestra.update()

    binary_prob_tree(x2_p1, y2_p1, level+1)
    binary_prob_tree(x2_p2, y2_p2, level+1)


canvas.create_line(300, 600, 300, 570, fill=colors[1], width= 5)
binary_prob_tree(300, 570, 1)


finestra.mainloop()