# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:20:28 2021

@author: india
"""

import random
from tkinter import *

window=Tk()
window.geometry("300x300")
window.title=("Dice")

l1=Label(window,text='',font=("times",80),bg='yellow')

def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}')

    l1.pack()

b1=Button(window,text="Lets roll..",command=roll,font=("arial",10),bg='blue')
b1.place(x=120,y=0)

window.mainloop()