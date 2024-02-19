import tkinter as tk
class app:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow

        tk.Label(mainwindow,text='Enter number of lines').pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.click = tk.Button(mainwindow,text='Check',command=self.action)
        self.click.pack()
        
        self.outLabel = tk.Label(mainwindow, text='')
        self.outLabel.pack()


    def action(self):
        data=int(self.name_entry.get())
        st=''
        for i in range(1,data+1):
            for j in range(1,i+1):
                st=st+str(j)
            st=st+'\n'
        self.outLabel.config(text=st)
root= tk.Tk()
exc=app(root)
root.mainloop()