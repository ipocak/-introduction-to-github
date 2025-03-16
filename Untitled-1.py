import csv
import numpy as np
from tkinter import * 
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import os

is_on1=True
is_on2=True


files=[]
for i in os.listdir():
    if i.endswith(".csv"):
        files.append(i)

def file(name):
    print(name)
    cadeath = np.genfromtxt(name, delimiter="," , dtype=object) 
    a = cadeath[:, 0].astype(int)
    b = cadeath[:, 1].astype(int) 
    c = cadeath[:, 2].astype(int) 
    d = cadeath[:, 3].astype(int) 
    return a,b

def plot(a,b,t):
    global is_on1
    fig1 = Figure(figsize = (5, 2), dpi = 100) 
    plot1 = fig1.add_subplot(111)
    plot1.plot(a,b)
    canvas1 = FigureCanvasTkAgg(fig1, master = window) 
    if is_on1:  
        canvas1.draw() 
        canvas1.get_tk_widget().place(x=500,y=20+t)
        is_on1=False
    else:
        for item in canvas1.get_tk_widget().find_all():
            canvas1.get_tk_widget().delete(item)
        is_on1=True
    print(is_on1)
               
        
def check(x,y,table):
   i=0
   for i in range(len(y)):
        if y[i]>3:
            table.insert(parent='',index='end', iid=i,text="s1", values=(x[i])) 
            i=i+1   

def selectrow(event):
    rowid=fl.identify_row(event.y)
    tag=fl.item(rowid)
    check(*file((tag["text"])))

window = Tk() 
window.geometry('1000x500')
#file(files[0])
#file(files[1])

table=ttk.Treeview(window)
table['columns']=('Time')
table.column("#0", width=50)
table.column("Time",anchor=W,width=120, minwidth=25)
table.heading("#0",anchor=W, text="File")
table.heading("Time", text="Time",anchor=W)

table.bind("<Double-Button>", selectrow)

fl=ttk.Treeview(window)
fl.column("#0",width=100)
fl.heading("#0", text="File",anchor=W)
fl.bind("<Double-Button>", selectrow)  

for i in range(len(files)):
    fl.insert(parent='',index='end', iid=i,text=files[i])  


[a,b,c,d]=file(files[2])
check(a,b,table)

p1=Button (master=window, text="wykres",command=lambda:plot(a,b,0))
p2=Button (master=window, text="wykres",command=lambda:plot(a,c,200))
p1.place(x=400, y=20)
p2.place(x=400, y=45)
table.place(x=140, y=20)
fl.place(x=20, y=20)
window.mainloop()