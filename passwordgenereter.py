import tkinter as tk
import random
class password:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow
        tk.Label(mainwindow,text='Password generater',font=('bold',20),fg='orange').grid(row=0,column=0)
        tk.Label(mainwindow,text='Enter length of your password',font=('bold',12),fg='green').grid(row=2,column=0)
        self.entry=tk.Entry()
        self.entry.grid(row=2,column=1)
        tk.Label(mainwindow,text='# Please select the password type you want to generate',font=('bold',9),fg='sky blue').grid(row=3,column=0)
        
        self.selected_option=tk.StringVar()
        self.bt1=tk.Radiobutton(mainwindow,text='Strong',value='strong', variable=self.selected_option ,font=(4))
        self.bt1.grid(row=4,column=0)
        self.bt1=tk.Radiobutton(mainwindow,text='Medium',value='medium',variable=self.selected_option,font=(4))
        self.bt1.grid(row=5,column=0)
        self.bt1=tk.Radiobutton(mainwindow,text='Easy',value='easy',variable=self.selected_option,font=(4))
        self.bt1.grid(row=6,column=0)

        self.bt=tk.Button(text='Generate',font=(5),command=self.generate)
        self.bt.grid(row=7,column=0)

        self.outLabel=tk.Label(mainwindow,text='',font=('italic',14))
        self.outLabel.grid(row=8,column=0)


    def generate(self):
        password_length = int(self.entry.get())
        data= self.selected_option.get()

        if data == 'strong':
            char='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890@#$%&*()_-=+/<>/'
        elif data== 'medium':
            char='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
        elif data== 'easy':
            char='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'

        generated_password=''.join(random.choice(char) for i in range(password_length))

        self.outLabel.config(text=f'your password:{generated_password}')

if __name__=='__main__':
    root=tk.Tk()
    root.title("Password Generater")
    root.geometry('500x400')
    exc=password(root)
    root.mainloop()



