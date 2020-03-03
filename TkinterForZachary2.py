#import sys, os, serial, time,re,datetime
#import matplotlib.pyplot as plt
#import numpy as np
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image


''''********Global Variables**********'''
picname='default.png'

#This function gets a picture and puts it in a format that can be stuck in a label
def GetCurrentPic(mypic):
    imgref = Image.open(mypic)
    width,height=imgref.size
    width=int(round(width*.75))
    height=int(round(height*.75))
    imgref = imgref.resize((width, height), Image.ANTIALIAS)
    img=ImageTk.PhotoImage(imgref)
    imgref.close()
    return(img)

#This function takes whatever is in the entrybox and puts it in the l1 label box
def mirrorinput():
    message=entrybox.get()
    l1.config(text=message)
    entrybox.delete(0,tk.END)
    return()

master=tk.Tk() #This creates the master
#master.geometry('1000x700')

entrybox=tk.Entry(master, borderwidth=2, relief="groove") #The box is 50 pixels wide
entrybox.focus()#says put cursor in entry box
entrybox.grid(row=0,column=0)

l1=tk.Label(master, text="Enter an adjective here", borderwidth=2, relief="groove",width=25, fg='white',bg='black')
l1.grid(row=0,column=1)


btnentry=tk.Button(master,text="Press me to mirror input", command=mirrorinput)
#For some reason master.destroy hangs up but master.quit works?!?!?!?
btnentry.grid(row = 1, column=0)
btnend=tk.Button(master,text="I'm the QUIT Button", command=master.destroy)
#For some reason master.destroy hangs up but master.quit works?!?!?!?
btnend.grid(row = 1, column=1)

master.mainloop() #start running it
#Here we make an entry box for our filename
'''topframe=tk.Frame(master, bd=3)
topframe.grid(row=0,column=0,columnspan=2,sticky='nsew')
borderframe1=tk.Frame(master)
borderframe1.grid(row=1,column=0,columnspan=2,)
middleframe=tk.Frame(master,bd=3)
middleframe.grid(row=2,column=0,columnspan=2,sticky='nsew')
borderframe2=tk.Frame(master)
borderframe2.grid(row=3,column=0,columnspan=2,)
leftbottomframe=tk.Frame(master,bd=3)
leftbottomframe.grid(row=4,column=0,sticky='nsew')
rightbottomframe=tk.Frame(master,bd=3)
rightbottomframe.grid(row=4,column=1,sticky='nsew')

#Items in the TOP frame
l1=tk.Label(topframe, text="Enter a file description here:")
l1.grid(row=0,column=0)
entrydescr=tk.Entry(topframe,width=50,bd=3) #The box is 50 pixels wide
entrydescr.insert(0,filename)
entrydescr.focus()
entrydescr.grid(row=0,column=1,sticky='nsew')
l2=tk.Label(topframe,text='Pick your COM port')
l2.grid(row=1,column=0,sticky='nsew')
combo = TTK.Combobox(topframe) #For some reason a combo box lives in a different library.
                            #It is called with TTK. See import at the top of the file

combo['values']=ports #This has to be a tuple. I populated this at the very beginning of the file
combo.current(10)
combo.grid(row=1,column=1,sticky='nsew')
combo.bind("<>", initcom)
l_adc=tk.Label(topframe, text="Enter an ADC scale factor here:")
l_adc.grid(row=2,column=0,sticky='nsew')
entry_adc=tk.Entry(topframe,width=50,bd=3) #The box is 50 pixels wide
entry_adc.insert(0,str(newtonscale))
entry_adc.grid(row=2,column=1,sticky='nsew')

#Serial readback window
entryreadback=tk.Entry(topframe,width=50)
entryreadback.grid(row=1,column=2,sticky='nsew',padx=100)#how do I make a column 60 wide? and put a 50 width item in it?
buttonconnect=tk.Button(topframe,text='Connect',bd=3,command=initcom)
buttonconnect.grid(row=3,column=1,sticky='nsew')


#Widget for the borderframe1
lborder1=tk.Label(borderframe1,text='  ')
lborder1.pack()

#Itemsin the Middle Frame
entrysamples=tk.Entry(middleframe,width=50,bd=3)
entrysamples.grid(row=0,column=0,sticky='nsew')
buttonsamples=tk.Button(middleframe,text='Change # of Samples',bd=3, command=changenumsamples)
buttonsamples.grid(row=1,column=0,sticky='nsew')

entrytime=tk.Entry(middleframe,width=50,bd=3)
entrytime.grid(row=0,column=1,sticky='nsew')
buttontime=tk.Button(middleframe,text='Change Sample Time',bd=3,command=changesampletime)
buttontime.grid(row=1,column=1,sticky='nsew')

entryaverage=tk.Entry(middleframe,width=50,bd=3)
entryaverage.grid(row=0,column=2,sticky='nsew')
buttonaverage=tk.Button(middleframe,text='Get Average',bd=3,command=getaverage)
buttonaverage.grid(row=1,column=2,sticky='nsew')


#Widget for the borderframe2
lborder2=tk.Label(borderframe2,text=' ')
lborder2.pack()
#Here is our GO button
buttonrawdata=tk.Button(leftbottomframe,text="Get Raw Data", command=getrawdata,width=25)
buttonrawdata.grid(row = 0, column=0)
#Here is our quit button

img=GetCurrentPic(picname)
plotteddata = tk.Label(rightbottomframe, image = img)
plotteddata.grid(row=0,column=1,rowspan=2)
#sz=master.grid_size() #how big is our grid


btnend=tk.Button(leftbottomframe,text="QUIT", command=alldone,width=5)
#For some reason master.destroy hangs up but master.quit works?!?!?!?
btnend.grid(row = 1, column=0)
'''
master.mainloop() #start running it
