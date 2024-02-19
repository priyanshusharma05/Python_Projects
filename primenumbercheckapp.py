import tkinter as tk
class app:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow

        tk.Label(mainwindow,text='Emter Your Number you want to check').pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.click = tk.Button(mainwindow,text='Check',command=self.action)
        self.click.pack()
        
        self.outLabel = tk.Label(mainwindow, text='')
        self.outLabel.pack()

    def action(self):
        data=int(self.name_entry.get())
        # if data<=7 and data%2!=0 :
        #      self.outLabel.config(text='Prime Number')
        # elif data==2:
        #     self.outLabel.config(text='Prime Number')
        # for i in range(2,int((data+1)**0.5)):
        #     if  data%i!=0:
        #       self.outLabel.config(text='Prime Number')
        #     else:
        #         self.outLabel.config(text='Not Prime Number')

root= tk.Tk()
exc=app(root)
root.mainloop()