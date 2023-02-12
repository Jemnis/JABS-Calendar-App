from tkinter import*
from tkinter import messagebox
import sqlite3
import os

win= Tk()
win.minsize(450,550)
win.minsize(450,550)
win.resizable(False, False)
win.title("JABS Calender (NOTES)")  #window title
win.iconbitmap("calender.ico")
theme_a=('helvetica',12,'bold')   
theme_b=('helvetica',12) 

def show():
    global show_lbl
    note = sqlite3.connect('notepad.db')
    c=note.cursor()
    c.execute("SELECT *, oid FROM data")
    records = c.fetchall()
    print(records)
    print_record = ''
    for record in records:
        print_record += str(f"""{str(record[2])}. {record[0]}""") +"\n"

    show_lbl = Label(winframe,text=print_record,bg="white",fg="black")
    show_lbl.place(x=100,y=200)
    note.commit()
    note.close()

def delete():
    note = sqlite3.connect('notepad.db')
    c=note.cursor()
    c.execute("DELETE from data WHERE oid = " + delete_box.get())
    messagebox.showinfo("jabs notes","delete sucessfully")
    delete_box.delete(0,END)
    show_lbl.destroy()         #to clear the show data in the window 
    note.commit()
    note.close()
    
def update():
    note=sqlite3.connect('notepad.db')
    c=note.cursor()
    record_id= edit_box.get()
    c.execute("""UPDATE data set
    title=:title,
    note=:note_ent
    WHERE oid = :oid """,
    {'title':title_edit.get(),
    'note_ent':note_edit.get("1.0", "end"),
    'oid':record_id

    })
    messagebox.showinfo("Jabs notes","Updated Successfully")
    editing.destroy()
    edit_box.delete(0,END)

    note.commit()
    note.close()  

def edit():
    global editing
    editing = Tk()
    editing.title("EDIT NOTES")
    editing.iconbitmap('calender.ico')
    editing.minsize(450,550)
    editing.minsize(450,550)
    editing.resizable(False, False)

    note = sqlite3.connect('notepad.db')
    c = note.cursor()
    record_id = edit_box.get()
    c.execute("SELECT * FROM data WHERE oid= " + record_id)
    records = c.fetchall()

    global title_edit
    global note_edit

    winframe=Frame(editing, height=550,width=450,bg='black')
    winframe.place(x=0,y=0)

    #notes text
    note_edit=Text(winframe,height=15,width=40,font=theme_b)
    note_edit.place(x=50, y=140)


    title_lbl = Label(winframe,text="Notes Title :",font=theme_a,bg="black",fg="white")
    title_lbl.place(x=50, y=97)

    h1 = Label(winframe,text="JABS NOTES",font=theme_a,bg='#BA0101',fg="white")
    h1.place(x=0,y=0,height=60)

    #entry

    title_edit= Entry(winframe,font=theme_b,width=20)
    title_edit.place(x=150,y=92,height=30)
    
    for record in records:
        title_edit.insert(1,record[0])
        note_edit.insert(INSERT,record[1]) # FOR INSERTING  a value in text we have to insertveriable 
    
    #buttons
    submit_btn = Button(winframe,text="update",cursor='hand2',width=11,font=theme_a,bg='#BA0101',relief=FLAT,fg='white',command=update)
    submit_btn.place(x=300,y=450,height=35)
 
    note.commit()
    note.close()       

def exit():
    win.destroy()
    os.system('python newnotes.py')

winframe=Frame(win, height=550,width=450,bg='black')
winframe.place(x=0,y=0)

h1 = Label(winframe,text="JABS NOTES",font=('helvetica',35,'bold'),bg='#800000',fg="white",width=16)
h1.place(x=0,y=0,height=60)

showrec_btn = Button(winframe,text="Show Records",cursor='hand2',bg="white",fg="black",font=theme_a,command=show)
showrec_btn.place(x=175,y=100)
 
quit_btn = Button(winframe,text="Quit",bg="white",cursor='hand2',fg="black",font=theme_a,command=exit)
quit_btn.place(x=380,y=480)

edit_btn = Button(winframe,text="Edit",bg="white",cursor='hand2',fg="black",font=theme_a,command=edit)
edit_btn.place(x=215,y=480)

edit_box=Entry(winframe,width=2,font=theme_b)
edit_box.place(x=190,y=480,height=33)

del_btn = Button(winframe,text="Delete",bg="white",cursor='hand2',fg="black",font=theme_a,command=delete)
del_btn.place(x=50,y=480)

delete_box=Entry(winframe,width=2,font=theme_b)
delete_box.place(x=25,y=480,height=33)

win.mainloop()