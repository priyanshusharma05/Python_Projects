from tkinter import *
#mainwindow
root= Tk()
root.geometry('200x100')
root.title("counter app")
#globalintilization
var= IntVar(value=0)
#actions
def fun1():
   data= var.get() + 1
   var.set(data)
   if data>= 10:
       lb.config(fg='red')
   else:
       lb.config(fg='green')
def fun2():
        data= var.get() - 1
        if data>=0:
          var.set(data)
        if data>= 10:
            lb.config(fg='red')
        else:
            lb.config(fg='green')

lb= Label(root,textvariable=var,font=('bold', 25),fg='pink',background='orange')
lb.pack()
butt1= Button(root, text='Increment', command=fun1)
butt1.pack(side=LEFT, ipadx=12,ipady=12, padx=13, pady=13)
butt2= Button(root, text='Decrement', command=fun2)
butt2.pack(side=RIGHT,ipadx=12,ipady=12, padx=13, pady=13)
root.mainloop()
