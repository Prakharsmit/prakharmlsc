import mysql.connector
from tkinter import*
from tkinter import messagebox
w0=Tk()
w0.geometry("580x250+350+175")
w0.title(" DELETE RECORD ")
w0.config(bg="grey89")
#   LABELS
la1=Label(text=" ENTER ANY ONE DETAIL--- ",bg='grey89',fg='black',font=('bold',16))
la1.place(x=180,y=25)
la2=Label(text="TEMPLE CODE:",bg='grey89',fg='black',font=('bold',14))
la2.place(x=70,y=75)
la3=Label(text="TEMPLE NAME :",bg='grey89',fg='black',font=('bold',14))
la3.place(x=70,y=140)
#  ENTRIES
e1=Entry(w0,width=30,bd=4)
e1.place(x=340,y=74)
e2=Entry(w0,width=30,bd=4)
e2.place(x=340,y=140)
def regi(a,b):
    con=mysql.connector.connect(host='localhost',user ='root',database='maindb')
    cur=con.cursor()
    cur.execute(f"delete from  temple  where TCode={a} or templenm= '{b}' ")
    con.commit()
    messagebox.showinfo(' DELETE RECORD '," RECORD DELETED ")
    e1.delete(0,'end')
    e2.delete(0,'end')
def reg():
    a=int(e1.get())
    b=e2.get()
    regi(a,b)
def a():
    w0.destroy()
    import aedit1
#  BUTTON
b1=Button(w0,text='DELETE',width=20,bd=4,fg='black',bg='grey89',command=reg)
b1.place(x=330,y=205)
b2=Button(w0,text='BACK',width=20,bd=4,fg='black',bg='grey89',command=a)
b2.place(x=110,y=205)
w0.mainloop()