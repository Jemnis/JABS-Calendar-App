# importing modules
from tkinter import*
import sqlite3
from tkinter import messagebox
import os
# creating window
win = Tk()
win.title("JABS CALENDER USER PROFILE")
win.minsize(340,430)
win.resizable(False, False) #making it unresizeable
theme=('helvetica',12,'bold')
theme2=('helvetica',12,)
win.configure(bg="black")

#This function calls profile module
def omkey():
    os.system('python Profile.py')

def back():
    win.destroy()
    os.system('python dashframe.py')

#This functoin logouts the user nad takes back to login page
def logout():
    msg = messagebox.askquestion("JABS CALENDER","Are you sure want to Log out?",icon="question")
    if msg == 'yes' :
            conn=sqlite3.connect('jabs.db') #Turning off hte user status
            c=conn.cursor()
            c.execute("""UPDATE users SET
            status= :off
            WHERE status= :on""",
            {
                'off':False,
                'on':True
            })
            conn.commit()
            conn.close()
            try:
                win.destroy()
                os.system('python login.py')
            except:
                pass
    else:
        pass
        
conn = sqlite3.connect('jabs.db')
c = conn.cursor()
c.execute("SELECT * FROM users")
records = c.fetchall()

#This function deletes the account from db
def delete():
    conn = sqlite3.connect("jabs.db")
    c = conn.cursor()
    c.execute("""UPDATE users SET
    status= :off
    WHERE status= :on""",#Turning off the user status
    {
        'off':False,
        'on':True
    })
    conn.commit()
    conn.close()
    conn = sqlite3.connect("jabs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    records = c.fetchall()
    for record in records:
        if rec[2] == record[2]:
            Msg = messagebox.askquestion('Delete Account','Are you sure you want to delete your account?', icon ='warning')
            if Msg == 'yes':
               c.execute("""DELETE from users WHERE email=:email""", #deleting the account
                {'email': rec[2]
                })
               messagebox.showinfo("Delete","Deleted Sucessfully!")
               conn.commit()
               conn.close()
               win.destroy()
               break
            else:
                pass
    else:
        messagebox.showerror("Error","Unable to delete")

#This fucntion displays the user info   
def info():
    global ok
    ok = Toplevel()
    ok.geometry("420x350")
    ok.title("Verify")
    ok.iconbitmap('calender.ico')
    ok.config(bg = "White")
    conn = sqlite3.connect('jabs.db')
    c=conn.cursor()
    c.execute(" SELECT * FROM users")

    #All the Labels
    fname = Label(ok, text=one1 , fg="Black",font=theme)
    fname.place(x=180, y=20,height=25)

    lname = Label(ok, text=two1, fg="Black",font=theme)
    lname.place(x=180, y=70,height=25)

    email = Label(ok, text=three1, fg="Black",font=theme)
    email.place(x=180,y=120,height=25)

    dob = Label(ok, text=four1, fg="Black",font=theme)
    dob.place(x=180, y=170,height=25)

    password = Label(ok, text=five1, fg="Black",font=theme)
    password.place(x=180,y=220,height=25)

    fname_lbl = Label(ok, text="First Name :-", width=15,fg="white",background='black',font=theme)
    fname_lbl.place(x=10, y=20)

    lname_lbl = Label(ok, text="Last Name :-",width=15,fg='white',background='black',font=theme)
    lname_lbl.place(x=10,y=70)

    email_lbl = Label(ok, text="Email :-",width=15,fg='white',background='black',font=theme)
    email_lbl.place(x=10, y=120)

    dob_lbl = Label(ok, text="Date of birth :-",width=15, fg='white',background='black',font=theme)
    dob_lbl.place(x=10,y=170)

    password_lbl = Label(ok, text="Password :-",width=15, fg="white",background='black', font=theme)
    password_lbl.place(x=10, y=220)
        
    Delete= Button(ok, text="Delete Account",cursor='hand2',fg='black',bg='Light grey',font=('helvetica',10,'bold'),relief=FLAT,width=13,command=delete)
    Delete.place(x=150,y=270,height=30)
   
#This function gets all the users info from the data base
def sev():
        global one1
        global two1
        global three1
        global four1
        global five1
        global six1
        global rec
        conn = sqlite3.connect('jabs.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        records = c.fetchall()
        for record in records:
            if record [2] == email_ent.get() and record [5]== security_ent.get():
                rec = record
                c.execute("""SELECT * FROM users WHERE email=:email""",
                {'email': email_ent.get()
                })
                one1 = record[0]
                two1= record[1]
                three1 = record[2]
                four1 = record[3]
                five1 = record[4]
                six1 = record[5]
                conn.commit()
                conn.close()
                info()
                break
        else:
            messagebox.showerror("JABS CALENDER","Your Email or Security answer does not Match") 
    
#LABLES
lbl=Label(win,text='Verify your Account',bg="#BA0101",fg='white',width=20,height=2,font=('helvetica',20,'bold'))
lbl.place(x=0,y=0)

lbl_eml=Label(win, text="Enter your email :",bg='black',fg='white',font=theme)
lbl_eml.place(x=50,y=100)

lbl_pass=Label(win, text='What is your best friend name?',bg='black',fg='white',font=theme)
lbl_pass.place(x=50,y=190)

# ENTRY    
email_ent=Entry(win,width=25,font=theme2)
email_ent.place(x=50,y=140,height=25)

security_ent=Entry(win,width=25,font=theme2)
security_ent.place(x=50,y=230,height=25)

#BUTTONS
Show_info = Button(win,text = "Show info" ,cursor='hand2',fg='black',bg='Light grey',font=('helvetica',10,'bold'),relief=FLAT,width=13, command=sev)
Show_info.place(x=15,y=300,height=30)

logout = Button(win, text="LogOut",fg="black",cursor='hand2',bg="Light grey",font=('helvetica',10,'bold'),relief=FLAT,width=13,command=logout)
logout.place(x=210,y=300,height=30)

back = Button(win,text="Back",fg="black",cursor='hand2',bg="Light grey",font=('helvetica',10,'bold'),relief=FLAT,width=13,command=back)
back.place(x=108,y=360,height=30)

win.mainloop()