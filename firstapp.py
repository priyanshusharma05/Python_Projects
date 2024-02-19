# GUI ==>>> GRAPHICAL USER INTERFACE
# import tkinter as tk
from tkinter import *

root = Tk()
root.geometry('2000x1000')
root.title('First App By priyanshu')
root.minsize(100,50)
root.maxsize(3000,2000)
def my_fun1():
    lb.config(text=lb.cget('text')+1)
def my_fun2():
    lb.config(text=lb.cget('text')-1)
  
lb = Label(root , text=0)
lb.pack()
bt1 = Button(root , text=' + ' , command=my_fun1)
bt1.pack()
bt2 = Button(root , text=' - ' , command=my_fun2)
bt2.pack()

root.mainloop()