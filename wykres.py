import csv
from tkinter import * 
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import os

files=[]
for i in os.listdir():
    if i.endswith(".csv"):
        files.append(i)
print(files)




def file(name):
    x = [] 
    y = [] 
    print(name)
    with open(name) as File: 
        print(File) 
        lines = csv.reader(File) 
        print(lines)        
        for row in lines: 
            x.append(row[0]) 
            y.append(int(row[1]))
    n=[]
    return x, y   

def check(x,y,table):
   i=0
   n=[]
   for i in range(len(y)):
        if y[i]>405:
            table.insert(parent='',index='end', iid=i,text="s1", values=(x[i])) 
            i=i+1   

          
def plot(x,y): 
    fig = Figure(figsize = (5, 5), dpi = 100) 
    plot1 = fig.add_subplot(111) 
    plot1.plot(x,y)    
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 
    canvas.get_tk_widget().pack(width=50,heigh=20 ,side=RIGHT,)
    del x[:]
    del y[:] 
    #toolbar = NavigationToolbar2Tk(canvas,window) 
    #toolbar.update() 
    #canvas.get_tk_widget().pack(side=RIGHT) 

window = Tk() 


table=ttk.Treeview(window)
table['columns']=('Time')
table.column("#0",width=120, minwidth=25)
table.column("Time",anchor=W,width=120, minwidth=25)

table.heading("#0", text="File",anchor=W)
table.heading("Time", text="Time",anchor=W)

table.insert(parent='',index='end', iid=0, text="s1", values=(123))


w=Radiobutton(pady=5)

#window.geometry("500x500") 
#plot_button = Button(master = window,command = plot(*file(files[0])),height = 2, width = 10,text = "Plot") 
#plot_button.pack()
table.pack(side=LEFT)
check(*file(files[0]),table)
plot(*file(files[0]))   
window.mainloop()