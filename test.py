import csv
import numpy as np
from tkinter import * 
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import os

files=[]
n=[400,401,403]
k=['blue','red','green']
window = Tk()
window.geometry('770x550')

fl=ttk.Treeview(window)
fl.column("#0",width=100)
fl.heading("#0", text="File",anchor=W)

table=ttk.Treeview(window)
table['columns']=('Time')
table.column("#0", width=50)
table.column("Time",anchor=W,width=120, minwidth=25)
table.heading("#0",anchor=W, text="File")
table.heading("Time", text="Time",anchor=W)

var1 = Label(window, text = 'var1', font=('calibre',10, 'bold'))
var2 = Label(window, text = 'var2', font=('calibre',10, 'bold'))
var3 = Label(window, text = 'var3', font=('calibre',10, 'bold'))
ent1=Entry(window, textvariable = n[0], font = ('calibre',10,'normal'))
ent2=Entry(window, textvariable = n[1],  font = ('calibre',10,'normal'))
ent3=Entry(window, textvariable = n[2], font = ('calibre',10,'normal'))


for i in os.listdir():
    if i.endswith(".csv"):
        files.append(i)
        
for i in range(len(files)):
    fl.insert(parent='',index='end', iid=i,text=files[i])  
                      
def selectr1(event):
    rowid=fl.identify_row(event.y)
    tag=fl.item(rowid)
    file(tag['text'])
    
def selectr2(event):
    rowid=table.identify_row(event.y)
    tag=table.item(rowid)
    fig(tag['values'],tag['text'])
    
def check(x,y,table):
   for i in range(len(y)):
        if y[i]>n:
            table.insert(parent='',index='end', iid=i,text="s1", values=(x[i])) 
            i=i+1   

def file(name):
    for item in table.get_children():
        table.delete(item)
    sig = np.genfromtxt(name, delimiter="," , dtype=object)
    a = sig[:, 0].astype(int)
    id=1
    for i in range(len(sig[2])-1):  
        b = sig[:,(i+1)].astype(int)
        for j in range(len(b)):
            if b[j]>n[i]:
                table.insert(parent='',index='end', iid=id,text=name, values=(a[j])) 
                id=id+1          

def fig(v,name):
    sig = np.genfromtxt(name, delimiter="," , dtype=object)
    a = sig[:, 0].astype(int)
    b = sig[:, 1].astype(int)
    fig = Figure(figsize = (3, 2), dpi = 100) 
    plot = fig.add_subplot(111)
    plot.plot(a,b)
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 
    canvas.get_tk_widget().place(x=350,y=20)

def openNewWindow():
    n=[]
    newWindow = Toplevel(window) 
    newWindow.title("Settings") 
    newWindow.geometry("200x200")
    var1 = Label(window, text = 'var1', font=('calibre',10, 'bold'))
    var2 = Label(window, text = 'var2', font=('calibre',10, 'bold'))
    var3 = Label(window, text = 'var3', font=('calibre',10, 'bold'))
    ent1=Entry(window, font = ('calibre',10,'normal'))
    ent2=Entry(window,  font = ('calibre',10,'normal'))
    ent3=Entry(window,  font = ('calibre',10,'normal'))


fl.place(x=20, y=20)
fl.bind("<Double-Button>", selectr1)          

var1.place(x=20, y=300)
var2.place(x=20, y=320)
var3.place(x=20, y=340)
ent1.place(x=60, y=300)
ent2.place(x=60, y=320)
ent3.place(x=60, y=340)

table.place(x=150, y=20)
table.bind("<Double-Button>", selectr2)   

#btn = Button(window,text ="Click to open a new window", command = openNewWindow)
#btn.pack(pady = 10)
      
window.mainloop()