from tkinter import*
from tkinter import messagebox
w3=Tk()
w3.config(bg='grey89')
w3.geometry("600x475+350+75")
w3.title(" DATA ADDITION FORM ")
#  LABELS
la1=Label(text=" -----TEMPLE DETAILS----- ",bg='grey89',fg='black',font=('bold',16))
la1.place(x=170,y=25)
la2=Label(text="CODE :",bg='grey89',fg='black',font=('bold',14))
la2.place(x=50,y=75)
la3=Label(text="TEMPLE NAME :",bg='grey89',fg='black',font=('bold',14))
la3.place(x=50,y=120)
la4=Label(text="STATE :",bg='grey89',fg='black',font=('bold',14))
la4.place(x=50,y=165)
la5=Label(text="DISTRICT :",bg='grey89',fg='black',font=('bold',14))
la5.place(x=50,y=210)
la6=Label(text="COUNTRY :",bg='grey89',fg='black',font=('bold',14))
la6.place(x=50,y=255)
la7=Label(text="ESTABLISHED ON (YYYY:MM:DD):",bg='grey89',fg='black',font=('bold',14))
la7.place(x=50,y=300)
la8=Label(text="FAMOUS FOR :",bg='grey89',fg='black',font=('bold',14))
la8.place(x=50,y=345)
#    ENTRIES
e1=Entry(w3,width=30,bd=4)
e1.place(x=370,y=74)
e2=Entry(w3,width=30,bd=4)
e2.place(x=370,y=119)
e3=Entry(w3,width=30,bd=4)
e3.place(x=370,y=164)
e4=Entry(w3,width=30,bd=4)
e4.place(x=370,y=209)
e5=Entry(w3,width=30,bd=4)
e5.place(x=370,y=254)
e6=Entry(w3,width=30,bd=4)
e6.place(x=370,y=299)
e7=Entry(w3,width=30,bd=4)
e7.place(x=370,y=345)
def pidea(a,b,c,d,e,f,g):
    import mysql.connector
    con=mysql.connector.connect(host='localhost',user='root')
    cur=con.cursor()
    cur.execute('create database if not exists maindb')
    cur.execute('use  maindb')
    qry='''create table if not exists temple
    ( TCode                    int Not null  unique,
    Templenm            varchar(30),
    state               varchar(20),
    district            varchar(15),
    country             varchar(15),
    established_on      date,
    attraction          varchar(100));
    '''
    cur.execute(qry) 
    con1=mysql.connector.connect(host='localhost',user='root',database='maindb')
    cur1=con1.cursor()
    qy=f"""insert into temple
    values({a},'{b}','{c}','{d}','{e}','{f}','{g}');
    """
    cur1.execute(qy)
    con1.commit()
def pr():
    w3.destroy()
    import aedit2
def regi():
    try:
        a=int(e1.get())
        b=e2.get()
        c=e3.get()
        d=e4.get()
        e=e5.get()
        f=e6.get()
        g=e7.get()
        pidea(a,b,c,d,e,f,g)
        messagebox.showinfo('Registration ',"Registered ")
        e1.delete(0,'end')
        e2.delete(0,'end')
        e3.delete(0,'end')
        e4.delete(0,'end')
        e5.delete(0,'end')
        e6.delete(0,'end')
        e7.delete(0,'end')
    except:
        messagebox.showinfo("ERROR","TCODE ALREADY EXISTS ")
        e1.delete(0,'end')
#  BUTTON
b1=Button(w3,text='REGISTER',width=20,bd=4,fg='black',bg='grey89',command=regi)
b1.place(x=370,y=410)
b2=Button(w3,text='BACK',width=20,bd=4,fg='black',bg='grey89',command=pr)
b2.place(x=100,y=410)
w3.mainloop()