from tkinter import*
from tkinter import messagebox , ttk
w2=Tk()
w2.config(bg='black')
w2.geometry("600x400+350+75")
w2.title(" LOGIN FORM ")
#  LABELS
la1=Label(text=" LOGIN DETAILS ",bg='white',fg='red',font=('bold',16))
la1.place(x=200,y=25)
la4=Label(text="USERNAME :",bg='white',fg='indigo',font=('bold',14))
la4.place(x=50,y=145)
la5=Label(text="PASSWORD :",bg='white',fg='indigo',font=('bold',14))
la5.place(x=50,y=195)
la6=Label(text="SELECT ONE :",bg='white',fg='indigo',font=('bold',14))
la6.place(x=50,y=250)
de=["ADMIN","USER"]
c=ttk.Combobox(w2, width=20, values=de )
c.place(x=370,y=250)
c.current(1)
#ENTRIES
e1=Entry(w2,width=30,bd=4)
e1.place(x=370,y=145)
e2=Entry(w2,width=30,bd=4,show='*')
e2.place(x=370,y=195)
#BUTTON
def sign():
    w2.destroy()
    import ak_user_register_form
def pre():
    w2.destroy()
    import testwel1
def checkpass():
    global c
    if c.get()=="ADMIN" :
        try:
            u=e1.get()
            p=e2.get()
            f=open('loginfo.txt')
            s=f.readlines()
            #print(s)   ("for all details saved in registration")
            f.close()
            s=list(s)
            mila=False
            for rec in s:
                r=rec.split(',')
                if r[6]==u and r[7]==p:
                    mila=True
                    break
            if mila==True:
                 e1.delete(0,'end')
                 e2.delete(0,'end')
                 messagebox.showinfo('Login  ',"Login Successful Right Password  ")
                 w2.destroy()
                 import aedit
            else:
                 messagebox.showinfo('Login  ',"Wrong  Password  ")
                 e1.delete(0,'end')
                 e2.delete(0,'end')
        except:
            messagebox.showinfo("INFO","Try Again Or Register First")
            e1.delete(0,'end')
            e2.delete(0,'end')
    else :
        messagebox.showinfo("INFO","User Can't Modify")
        pre()
b1=Button(w2,text=' LOGIN ',width=20,bd=4,fg='white',bg='black',command=checkpass)
b1.place(x=212,y=305)
b2=Button(w2,text=' SIGN UP ',width=20,bd=4,fg='white',bg='black',command=sign)
b2.place(x=370,y=350)
b3=Button(w2,text=' BACK ',width=20,bd=4,fg='white',bg='black',command=pre)
b3.place(x=50,y=350)
w2.mainloop()