from tkinter import*
import sqlite3
from tkinter import messagebox
import os

# creating window
win= Tk()
win.minsize(450,550)
win.minsize(450,550)
win.resizable(False, False)        # resizable is false so that the windo cannot be minimixe or maximizes
win.title("JABS Calender (NOTES)")  #window title
win.iconbitmap("calender.ico")
win.config(bg="Black")
theme_a=('helvetica',12,'bold')   
theme_b=('helvetica',12,)  

#creating a database for note
note=sqlite3.connect('notepad.db')
#crearinga a cursor
n=note.cursor()       #it is an instance which can invoke methord that exuicate SQLite statementfetch data from the tesult set quaries
# # creatind data base table
try:
    n.execute(""" CREATE TABLE data(
        title text,
        note text

    ) """)
    note.commit()
    note.close()
except:
    pass

def submit():
    if note.get("1.0", "end") == '' :
        messagebox.showerror("JABS Notes","Your notes box is empty")
    elif title_ent.get() == '' :
        messagebox.showerror("JABS NOTES","your notes title is empty")
    else:
        con = sqlite3.connect('notepad.db')
        c= con.cursor()
        c.execute("INSERT INTO data VALUES(:title,:note)",
        {
        'title':title_ent.get(),
        'note':note.get("1.0", "end")
        })
        messagebox.showinfo("JABS CALENDER","Notes saved succesfully")
        title_ent.delete(0,END)
        note.delete("1.0", "end")
        con.commit()
        con.close()

def exit():
    win.destroy()

def show_list():
    win.destroy()
    os.system('python query.py')

#notes text
note =Text(win,height=15,width=40,font=theme_b)
note.place(x=50, y=175)

#lable
title_lbl = Label(win,text="Notes Title :",font=theme_a,bg="black",fg="white")
title_lbl.place(x=50, y=107,height=35)
h1 = Label(win,text="JABS E-NOTE",font=('helvetica',20,'bold'),width=27,bg='#BA0101',fg="white")
h1.place(x=0,y=0,height=60)

#entry
title_ent= Entry(win,font=theme_b,width=15)
title_ent.place(x=150,y=107,height=35)

#buttons
submit_btn = Button(win,text="Submit",width=11,font=theme_a,cursor='hand2',bg='#BA0101',relief=FLAT,fg='white',command=submit) # relief=FLAT it is a style 
submit_btn.place(x=300,y=475,height=35)

query = Button(win,text="Show Lists",width=9,font=theme_a,cursor='hand2',bg='#BA0101',relief=FLAT,fg='white',command=show_list)
query.place(x=313,y=107,height=35)

exit_btn = Button(win,text="Exit",width=11,font=theme_a,cursor='hand2',bg='#BA0101',relief=FLAT,fg='white',command=exit)
exit_btn.place(x=50,y=475,height=35)

win.mainloop()


