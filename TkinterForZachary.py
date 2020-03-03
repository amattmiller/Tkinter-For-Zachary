#import sys, os, serial, time,re,datetime
#import matplotlib.pyplot as plt
#import numpy as np
from tkinter import ttk
import tkinter as tk

def mirrorinput():
    message=entrybox.get()
    l1.config(text=message)
    return()

master=tk.Tk()

entrybox=tk.Entry(master, borderwidth=2, relief="groove") #The box is 50 pixels wide
entrybox.focus()#says put cursor in entry box
entrybox.grid(row=0,column=0)
l1=tk.Label(master, text="Stuff will get mirrored here", borderwidth=2, relief="groove")
l1.grid(row=0,column=1)

btnentry=tk.Button(master,text="Press me to mirror input", command=mirrorinput)
btnentry.grid(row=1, column=0)

btnend=tk.Button(master,text="I'm the QUIT Button", command=master.destroy)
btnend.grid(row=1, column=1)

master.mainloop() #start running it
