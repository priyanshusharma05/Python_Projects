import tkinter as tk

class app:
    def __init__(self, mainwindow):
        self.mainwindow=mainwindow


        tk.Label(mainwindow, text='Enter your name',font=('BOLD',20),bg='pink').pack(ipadx=2,ipady=2,padx=4,pady=4)

        self.name_entry = tk.Entry(root)
        self.name_entry.pack(ipadx=5,ipady=5)

        self.click = tk.Button(mainwindow,text='Enter',command=self.action)
        self.click.pack()

        self.outLabel = tk.Label(mainwindow, text='')
        self.outLabel.pack()
        root.configure(bg='blue')  

        self.mainwindow.geometry('200x100')

    def action(self):
        data= self.name_entry.get()
        self.outLabel.config(text='Welcome into <HELL> Mr.' +data,font=('BOLD',20),bg='aqua')
        self.name_entry.delete(0,  tk.END)
        root.configure(bg='red')  
#main code
root=tk.Tk()
exc=app(root)
root.mainloop()        



























# root.geometry('200X100')
# root.title('Greeting App')



# lb=tk.Label(root,text=input("enter your name"))