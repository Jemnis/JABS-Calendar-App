# import modules
from tkinter import*
from tkinter import messagebox
import sqlite3

# create window
top=Tk()
top.minsize(400,400)    #window min size
top.resizable(False,False) #window resizable
top.iconbitmap("calender.ico")  #window icon
theme = ('helvetica',12,'bold') # font style
theme2=('helvetica',12,)        # font style
top.title('RESET PASSWORD (JABS CALENDER)')#window title

#framing
frm=Frame(top,bg='light gray',height=500,width=500).place(x=0,y=0)

#labaling 
lbl=Label(top, text='RESET PASSWORD', bg="#BA0101", fg='white', font=('helvetica',20,'bold'),width=24).place(x=0, y=0,height=47)
lbl_eml=Label(top, text="Email :",bg='light gray',fg='black',font=theme,width=15).place(x=5,y=80)
lbl_pass=Label(top, text='Password:',bg='light gray',fg='black',font=theme,width=15).place(x=5,y=200)
lbl_cpass=Label(top, text='Confirm\nPassword :',bg='light gray',fg='black',font=theme,width=15).place(x=5, y=240)

#entry widgets
email_ent=Entry(top,width=25,font=theme2)
email_ent.place(x=135,y=80,height=25)

security_ent=Entry(top,width=25,font=theme2)
security_ent.place(x=135,y=155,height=25)

pass_ent = Entry(top,width=25,font=theme2)
pass_ent.place(x=135,y=200,height=25)

cpass_ent= Entry(top,width=25,font=theme2)
cpass_ent.place(x=135,y=250,height=25)
       
# drop downs
security1 = StringVar()
security1.set("Security Questions")
drop = OptionMenu(top, security1, "What is your bestfriend name?",)
drop.configure(relief=FLAT,font=('helvetica',10,),cursor='hand2',)
drop.place(x=135, y=120,width=230,height=27)

#defining submit button
def submit1():
        pas=pass_ent.get()
        cpas = cpass_ent.get()

        conn = sqlite3.connect('jabs.db')
        c=conn.cursor()
        c.execute(" SELECT * FROM users")
        records = c.fetchall()

        for record in records:
            if (record [2] == email_ent.get()) and (record [5]== security_ent.get()):

                if len(pas) <= 5 and len(cpas) <= 5:
                        messagebox.showerror("JABS CALENDER","Password must be 6 letter or more")
                        break
                
                else:    
                        if (pass_ent.get() == cpass_ent.get()):
                                conn = sqlite3.connect('jabs.db')
                                c=conn.cursor()
                                c.execute("""UPDATE users SET confirm_password=:pass WHERE email =:email""",
                                {'pass': cpass_ent.get(),
                                'email':email_ent.get()
                                })
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("JABS CALENDER","Password Changed Sucessfully")
                                email_ent.delete(0,END)
                                security_ent.delete(0,END)
                                pass_ent.delete(0,END)
                                cpass_ent.delete(0,END)
                                top.destroy()
                                break
                        else:
                                messagebox.showerror("JABS CALENDER","Your PasswordDoes not Match")
                        
        else:
            messagebox.showerror("JABS CALENDER","Your Email or Security answer does not Match")

 #def function on exit

def exit():        
        top.destroy()

submit = Button(top,text='Submit',bg='black',fg='white',cursor='hand2',border=0,font=theme2,width=10,command=submit1)     #submit button
submit.place(x=260,y=325,height=35)

exit = Button(top, text="Exit",width=10,bg='black',fg='white',cursor='hand2',border=0,font=theme2,command=exit)   #exits buttons
exit.place(x=52,y=325,height=35)

top.mainloop()
