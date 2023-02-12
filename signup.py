# importing modules
from tkinter import*
import sqlite3
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime as dt
from datetime import date
import os

# creating window
root= Tk()
root.minsize(1280,720)  #minimun window size
root.title("JABS Calender Registration")  #window title
root.iconbitmap("calender.ico") #window icon
theme=('helvetica',12,'bold')   #theme 1
theme2=('helvetica',12,)     #theme 2
today = date.today()    #time

# bg image
bg=  PhotoImage(file= 'bg2.png')
bg_lbl = Label(root, image=bg)
bg_lbl.pack()

#Creating database
try:
    conn = sqlite3.connect('jabs.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE users(
        f_name text,
        lname text,
        email text,
        dob integer,
        confirm_password,
        security_ans text,
        status boolean
         )
        """)
except:
    pass 

# def function to show password
a=0
def showpass():
    global a
    a=a+1
    if a%2==0:
        password.config(show='*') or cpass.config(show="*")
    else:
        password.config(show='') or cpass.config(show='')

# defining register button
def submit():   
    a=fname.get()
    b=lname.get()
    c=email.get()
    d=dob.get()
    f=password.get()
    g=cpass.get()
    e=security.get()

    if a=='' or b=='' or c=='' or d=='' or e=='' or f=='' or g=='':
        messagebox.showerror("JABS Calender","You must fill all of the fields above.")
    
    elif "@" and ".com" not in c:
        messagebox.showerror("JABS CALENDER","Invalid Email")

    elif len(f) <= 5 and len(g) <= 5:
        messagebox.showerror("JABS CALENDER","Password must be 6 letters or more")
            
    elif f!=g:
        messagebox.showerror("JABS CALENDER","Password did not matched")

    else:
        conn = sqlite3.connect('jabs.db')   #connecting database
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES(:f_name,:lname,:email,:dob,:confirm_password,:security_ans,:status)",{
        'f_name':fname.get() ,
        'lname':lname.get(),
        'email':email.get(),
        'dob':dob.get(),
        'confirm_password':cpass.get(),
        'security_ans':security.get(),
        'status': False
        })
        messagebox.showinfo("JABS CALENDER","Sucessfully Created New Account")
        fname.delete(0,END)
        lname.delete(0,END)
        email.delete(0,END)
        dob.delete(0,END)
        password.delete(0,END)
        cpass.delete(0,END)
        security.delete(0,END)
        
        conn.commit()
        conn.close()

# defining login function to go in login window
def login():
    root.destroy()
    os.system('python login.py')
    
#frame one
winframe=Frame(root, height=530,width=420,bg='light gray').place(x=725,y=60)

# heading
lbl=Label(winframe,text='CREATE NEW ACCOUNT',bg="#BA0101",fg='white',width=23,font=('helvetica',20,'bold')).place(x=738,y=75,height=85)

# entry
fname = Entry(winframe,font=theme2,width=25)
fname.place(x=909, y=180,height=25)

lname = Entry(winframe, font=theme2,width=25)
lname.place(x=909, y=220,height=25)

dob = DateEntry(winframe,maxdate=today,width=15,font=theme2,)
dob.place(x=909, y=260,height=25)

email = Entry(winframe, font=theme2,width=25)
email.place(x=909,y=300,height=25)

password = Entry(winframe, font=theme2,width=18,show="*")
password.place(x=909,y=340,height=25)

cpass = Entry(winframe, font=theme2,width=18,show="*")
cpass.place(x=909, y=380,height=25)

security = Entry(winframe, font=theme2,width=25)
security.place(x=736, y=460,height=25,width=405)

# drop downs bar for security questions
security1 = StringVar()
security1.set("Security Question")
drop = OptionMenu(winframe, security1, "What is your bestfriend name?",)
drop.configure(relief=FLAT,font=theme,cursor='hand2')
drop.place(x=736, y=420,width=405,height=28)

# lables 
fname_lbl = Label(winframe, text="First Name :",anchor=W, width=15,fg="black",background='light gray',font=theme)
fname_lbl.place(x=736, y=180)

lname_lbl = Label(winframe, text="Last Name :",anchor=W,width=15,fg='black',background='light gray',font=theme)
lname_lbl.place(x=736,y=220)

email_lbl = Label(winframe, text="Email :",anchor=W,width=15,fg='black',background='light gray',font=theme)
email_lbl.place(x=736, y=300)

dob_lbl = Label(winframe, text="Date of birth :",anchor=W,width=15, fg='black',background='light gray',font=theme)
dob_lbl.place(x=736,y=260)

password_lbl = Label(winframe, text="Password :",width=15,anchor=W, fg="black",background='light gray', font=theme).place(x=736, y=340)

cpass_lbl = Label(winframe, text="Confirm Password :",anchor=W,width=15, fg='black',background='light gray',font=theme).place(x=736, y=380)

# bottons
registe_btn = Button(winframe, text="Register",width=13,font=theme,cursor='hand2',background='black',border=0,fg='white',command = submit)
registe_btn.place(x=1000, y=520,height=40)

back = Button(winframe, text="Back (LOGIN)",font=theme,background='black',cursor='hand2',fg='white',border=0,width=13,command=login)
back.place(x=750, y=520,height=40)

show = Button(winframe, text="Show",font=theme2,background='black',cursor='hand2',fg='white',border=0,command=showpass,height=2)
show.place(x=1087,y=340,height=66)

conn.commit()
conn.close()

root.mainloop()