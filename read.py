import csv
import numpy as np
from tkinter import * 
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import os

files=[]
for i in os.listdir():
    if i.endswith(".csv"):
        files.append(i)
               
def file(name):
    column = np.genfromtxt(name, delimiter="," , dtype=object) 
    a = column[:, 0].astype(int)
    b = column[:, 1].astype(int) 
    return a,b      

def plot(a,b):
    fig = Figure(figsize = (6, 5), dpi = 100) 
    plot = fig.add_subplot(111)
    plot.set_xlim(a[len(a)-101],a[len(a)-1])
    plot.plot(a,b)
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 
    canvas.get_tk_widget().place(x=150,y=20)

def selectrow(event):
    rowid=fl.identify_row(event.y)
    tag=fl.item(rowid)
    plot(*file((tag["text"])))
      
window = Tk()
window.geometry('770x550')
      
fl=ttk.Treeview(window)
fl.column("#0",width=100)
fl.heading("#0", text="File",anchor=W)
fl.place(x=20, y=20)
fl.bind("<Double-Button>", selectrow)  

for i in range(len(files)):
    fl.insert(parent='',index='end', iid=i,text=files[i])  

      
window.mainloop()