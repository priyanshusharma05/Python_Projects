import tkinter as tk
class app:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow

        mainwindow.configure(bg='sea green')

        tk.Label(text="To-Do List", font=('bold',20),bg='sea green').grid(row=0,column=0,padx=5,pady=5) 
        self.entry=tk.Entry(root)
        self.entry.grid(row=1,column=0, ipadx=4,ipady=4,padx=5,pady=5)

        self.bt=tk.Button(mainwindow,text="Add Item", command=self.additem, borderwidth=3,relief="groove",border=2, cursor='hand2')
        self.bt.grid(row=1,column=2,ipadx=2,ipady=2,padx=3,pady=3)
        
        self.listbox=tk.Listbox(root,width=25)
        self.listbox.grid(row=2,column=0,columnspan=2,ipadx=4,ipady=4,padx=6,pady=6)

        self.bt1=tk.Button(mainwindow,text="Remove Item",command=self.Removeitem,borderwidth=3,relief="groove",border=2, cursor='hand2')
        self.bt1.grid(row=3,column=1,ipadx=2,ipady=2,padx=3,pady=3)

        self.bt2=tk.Button(mainwindow,text="Remove All",command=self.removeall,borderwidth=3,relief="groove",border=2, cursor='hand2')
        self.bt2.grid(row=3,column=3,ipadx=2,ipady=2,padx=3,pady=3)

        self.bt3=tk.Button(mainwindow,text="Undo", command=self.undo,borderwidth=3,relief="groove",border=2, cursor='hand2')
        self.bt3.grid(row=3,column=0,ipadx=2,ipady=2,padx=3,pady=3)

        self.removeditem=None
        

    def additem(self):
        data=self.entry.get()
        self.listbox.insert(tk.END,data)
        self.entry.delete(0,tk.END)
    
    def Removeitem(self):
        try:
            index=self.listbox.curselection()
            self.removeditem=self.listbox.get(index[0])
            self.listbox.delete(index)
        except:IndexError
    
    def undo(self):
        self.listbox.insert(0,self.removeditem)
        self.removeditem=None

    def removeall(self):
        self.listbox.delete(0,tk.END)


root=tk.Tk()
exc=app(root)
root.title("To-Do List")
root.geometry('400x300')
root.mainloop()