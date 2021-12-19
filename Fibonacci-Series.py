# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 08:56:38 2021

@author: Lighthouse
"""

from tkinter import *
root=Tk()
root.title("Fibonacci")
root.geometry("400x400")
label_series=Label(root,text="FIBONACCI-SERIES:    ")
def fibonacci():
    num=10
    first_no=0
    second_no=1
    sum=0
    counter=1
    while(counter<=num):
        label_series["text"]+=str(sum)+" "
        counter=counter+1
        first_no=second_no
        second_no=sum
        sum=first_no+second_no
        



btn=Button(root,text="Show-Series",command=fibonacci)
btn.pack()
label_series.pack()


root.mainloop()