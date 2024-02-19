import tkinter as tk
from tkinter import messagebox
class app:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow
        mainwindow.configure(bg='aqua')
        tk.Label(mainwindow,text='BMI Calculator',font=('bold'),bg='aqua').grid(row=0,column=0)

        tk.Label(mainwindow,text='Weight',font=('bold'),bg='aqua').grid(row=1,column=0)
        self.entry1=tk.Entry(root)
        self.entry1.grid(row=1,column=1,columnspan=2)

        tk.Label(mainwindow,text='Height',font=('bold'),bg='aqua').grid(row=2,column=0)
        self.entry2=tk.Entry(root)
        self.entry2.grid(row=2,column=1,columnspan=2)

        self.bt=tk.Button(mainwindow,text='Check BMI',command=self.action,bg='aqua')
        self.bt.grid(row=4,column=1)

        self.outLabel=tk.Label(mainwindow,text='',bg='aqua')
        self.outLabel.grid(row=4,column=2)
    
    def action(self):
        a=float(self.entry1.get())
        b=float(self.entry2.get())
        c=a/(b**2)
        self.outLabel.configure(text=f'Your BMI is: {c:.2f}',font=('bold',15))

root=tk.Tk()
exc=app(root)
root.geometry('300x200')
tk.mainloop()