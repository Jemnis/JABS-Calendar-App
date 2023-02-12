# importing modules
from tkinter import*
import sqlite3
from tkinter import messagebox
import os
# creating window
root = Tk() 
root.minsize(1280,720)                  #window min size
root.iconbitmap("calender.ico")         #window icon
root.title("JABS Calender LogIn")       #window title
theme=('helvetica',12,'bold')           # fonts
theme2=('helvetica',12,)                # fonts

# bg image
bg=  PhotoImage(file= 'bg2.png')
bg_lbl = Label(root, image=bg)
bg_lbl.pack()

# define function for sign in button 
def signup():
    root.destroy()
    os.system('python signup.py')

#define function for log in button
def dashboard():
    email=email_entry.get()
    password=password_entry.get()

    if email=='' and password == '':
        messagebox.showerror("JABS CALENDER","Empty Fields,\nPlease enter your valid email and password.")
    
    else:
        conn = sqlite3.connect('jabs.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        records = c.fetchall()
        for record in records:
            if (record [2]  == email) and (record [4] == password):
                #change user status to active after login and set other users as inactive
                c.execute("""UPDATE users SET
                status=:inactive
                WHERE status=:active""",
                {'inactive':False,
                'active':True})
                conn.commit()   
                c.execute("""UPDATE users SET
                status= :val
                WHERE email = :a""",
                {
                    'val':True,
                    'a': email
                })
                conn.commit()
                messagebox.showinfo("JABS CALENDER","Login Sucessfully")
                root.destroy()
                os.system('python dashframe.py')
                break
                
                
        else:
            messagebox.showerror("JABS CALENDER","Incorrect email or password.\nPlease try again.  ")
           
#define function for forgrt password button               
def reset():
    os.system('python forgetpass.py')

# framing 
winframe=Frame(root, height=425,width=325,bg='black').place(x=850,y=120)

# heading
lbl=Label(winframe,text='SIGN IN',bg="#BA0101",fg='white',width=17,height=2,font=('helvetica',20,'bold')).place(x=865,y=130)

# data entry
email_entry = Entry(winframe, font=theme2, width=25)
email_entry.place(x=900,y=270,height=30)

password_entry = Entry(winframe,font=theme2,width=25,show="*")
password_entry.place(x=900,y=340,height=30)

#lables
emial_lbl = Label(winframe, text="E-mail",bg='black',fg="white",font=theme)
emial_lbl.place(x=986, y=245)

password_lbl = Label(winframe, text="Password",bg='black',fg="white",font=theme)
password_lbl.place(x=973,y=315)

sign_up = Label(winframe, text="Don't have an account?",bg='black',fg='white',font=('helvetica',10,))
sign_up.place(x=946,y=465)

#buttons 
forgot = Button(winframe, text="Forget Password?",fg='white',bg='black',font=('helvetica',9,'underline'),cursor='hand2',command=reset,relief=FLAT)
forgot.place(x=1024,y=375)

login = Button(winframe, text="Login",fg="black",bg="white",font=('helvetica',10,'bold'),cursor='hand2',relief=FLAT,width=12,command=dashboard)
login.place(x=960,y=414,height=30)

signup_btn = Button(winframe, text="CREATE NEW ACCOUNT",fg='white',bg='black',font=('helvetica',9,'underline'),cursor='hand2',relief=FLAT,command=signup)
signup_btn.place(x=940, y=490)

mainloop()