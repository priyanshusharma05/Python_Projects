import tkinter as tk
class app:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow

        tk.Label(text="Amount:-",font=('bold',15)).grid(row=0,column=0)
        tk.Label(text="# Enter the amount you want to convert",font=('sky blue',7),fg='blue').grid(row=1,column=0,columnspan=2)
        tk.Label(text="From:-",font=('bold',15)).grid(row=2,column=0)
        tk.Label(text="To:-",font=('bold',15)).grid(row=4,column=0)

        self.entry=tk.Entry()
        self.entry.grid(row=0,column=1)
        
        self.entry=tk.Entry()
        self.entry.grid(row=2,column=1)
    
        self.entry=tk.Entry()
        self.entry.grid(row=4,column=1)
        tk.Label(text="* Choose the currency among 'INR','USD', 'EUR', 'RIYAL','GBP' ",font=('green',7),fg='blue').grid(row=5,column=0,columnspan=2)
        
        self.bt=tk.Button(text="Convert", font=('bold',15),height=1,width=6, fg='yellow',bg='red', command=self.converter)
        self.bt.grid(row=6,column=1)

    def converter(self):
        pass
        

        

root=tk.Tk()
APP=app(root)
root.title("Currency converter")
root.geometry("500x400")
root.mainloop()