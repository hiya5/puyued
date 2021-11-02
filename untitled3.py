# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:45:39 2021

@author: Hiya Makhija
"""

from tkinter import*
import random

root=Tk()
root.title("list")

root.geometry("400x400")

random_number_list = Lable(root)
random_number_sorted_list = Lable(root)

def randomlist():
    randomlist = random.sample(range(10,30),5)
    random_number_list["text"] = "random list :"  + str(randomlist)
    randomlist.sort()
    random_number_sorted_list["text"] = "sorted random numbers : " + str(randomlist)
    
    btn=Button(root,text="genrate random list ",command=randomlist)
    btn.place(relx=0.5,rely=0.4,anchor=CENTER)
    
    random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
    random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)
    
    root.mainloop()