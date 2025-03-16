import csv
from tkinter import * 
import matplotlib.pyplot as plt 
x = [] 
y = [] 
with open('s1.csv') as File:  
    lines = csv.reader(File) 
    for row in lines: 
        x.append(row[0]) 
        y.append(int(row[1])) 
  
plt.plot(x, y)  
plt.xticks(rotation = 25) 
plt.xlabel('V') 
plt.ylabel('T') 
plt.title('EKG', fontsize = 20) 
plt.xlim(0,100)
plt.show() 