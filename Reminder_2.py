#firstly useful module are importef below
from tkinter import*
from tkinter import messagebox
import sqlite3

#creating our main window
win = Tk()
win.title("JABS REMINDER") 
win.minsize(400,450)
win.resizable(False,False)
win.attributes('-alpha',1)
win.iconbitmap('calender.ico')

try:
    conn = sqlite3.connect('Reminders_store.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE Event(
        event text,
        month text,
        day integer
        )""")
except:
    pass 

#This functions adds events to our data base
def subbmit():
    if Entry_Box.get() == "":
        messagebox.showerror("Error","Please, Enter your event in the box.")
    elif Entry_Box.get() == 'Enter Your Event Here:':
        messagebox.showerror("Error","Please type your event.")
    else:
        data = sqlite3.connect("Reminders_store.db") #creating data base
        c= data.cursor()
        c.execute("INSERT INTO Event VALUES(:event,:month,:day)",{ #Inserting values in our data base
        'event':Entry_Box.get(),
        'month':month.get() ,
        'day':day.get()
        })
        messagebox.showinfo("Dates","Inserted Sucessfully") #Message box shows a box with short messages
        Entry_Box.delete(0,END)
        data.commit()
        data.close()

#This function destroys our main window
def close():
    # win.destroy()
    win.quit()

#This function updates our reminders list
def update2():
        con = sqlite3.connect("Reminders_store.db")
        c = con.cursor()
        record_id = Events_List_Box.get()
        c.execute("""UPDATE Event SET 
        event = :event,
        month = :month,
        day = :day

        WHERE oid  = :oid""",
        {'event': Event_editor.get(),
        'month': Month_editor.get(),
        'day': Day_editor.get(),
        'oid' : record_id
            
            }
        )
        con.commit()
        con.close()
        editor.destroy()

#This functions checks wether the inputs are valid or not
def update():
    if int(Day_editor.get()) > 32 or int(Day_editor.get()) < 1:
        messagebox.showerror('Error','Please enter a valid day')
        editor.destroy()
    elif Month_editor.get().upper() == "JANUARY":
        update2()
    elif Month_editor.get().upper() == "FEBURARY":
        update2()
    elif Month_editor.get().upper() == "MARCH":
        update2()
    elif Month_editor.get().upper() == "APRIL":
        update2()  
    elif Month_editor.get().upper() == "MAY":
        update2()
    elif Month_editor.get().upper() == "JUNE":
        update2()
    elif Month_editor.get().upper() == "JULY":
        update2()
    elif Month_editor.get().upper() == "AUGUST":
        update2()
    elif Month_editor.get().upper() == "SEPTEMBER":
        update2()
    elif Month_editor.get().upper() == "OCTOBER":
        update2()
    elif Month_editor.get().upper() == "NOVEMBER":
        update2()
    elif Month_editor.get().upper() == "DECEMBER":
        update2() 
    else:
        messagebox.showerror('Error','Please enter a valid month')
        editor.destroy()
       
#This function opens up a new window where we can view our reminder list.
def edit():
    conn = sqlite3.connect("Reminders_store.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM Event") 
    records = c.fetchall()  #Getting all our record from Event table
    i = []
    for record in records:
        a = str(record[3])
        i.append(a)

    if Events_List_Box.get() == '':
        messagebox.showerror("Error","You must fill the event field")
    elif Events_List_Box.get() in i:
            global editor
            editor = Toplevel()
            editor.geometry("300x100")
            editor.title("Update Event Details")
            editor.resizable(False,False)
            editor.iconbitmap('calender.ico')
            conn = sqlite3.connect("Reminders_store.db")
            editor.config(bg = "black")
            c = conn.cursor()
            record_id = Events_List_Box.get()
            c.execute("SELECT * FROM Event WHERE oid= " + record_id)
            records = c.fetchall()
            
            global Event_editor
            global Month_editor
            global Day_editor
        

            Event_editor = Entry(editor, width = 30)
            Event_editor.grid(row = 0, column = 1, padx = 20, pady =(10,0))
        
            Month_editor = Entry(editor, width = 30)
            Month_editor.grid(row = 1, column = 1)
             
            
            Day_editor = Entry(editor, width = 30)
            Day_editor.grid(row = 2, column = 1)

            
        
            event_label= Label(editor, text = "Event Details",bg = 'black', fg = "white" ,font=("Helvetica",9,"bold"))
            event_label.grid(row = 0, column = 0)

            month_label= Label(editor, text = "Month",bg = 'black', fg = "white" ,font=("Helvetica",9,"bold"))
            month_label.grid(row = 1, column = 0)
            day_label= Label(editor, text = "Day",bg = 'black', fg = "white" ,font=("Helvetica",9,"bold"))
            day_label.grid(row = 2, column = 0)
        
            Save_it = Button(editor, text = "SAVE",font=("Helvetica",10,"bold"),cursor='hand2', fg = "black",bg = "white",border=0 ,command=update)
            Save_it.grid(row=3 , column = 1)
        

            for record in records:
                Event_editor.insert(0,record[0])
                Month_editor.insert(0,record[1])
                Day_editor.insert(0,record[2])
    else:
        messagebox.showerror("Error","Please enter a valid no.")

#This function delets our records from Event Table in our data base
def delete():
    conn = sqlite3.connect("Reminders_store.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM Event")
    records = c.fetchall()  
    i = []
    for record in records:
        a = str(record[3])
        i.append(a)
    
    if Events_List_Box.get() == '':
        messagebox.showerror("JABS CALENDER","You must fill the event field")

    elif Events_List_Box.get() in i:
        c.execute("DELETE from Event WHERE oid = " + Events_List_Box.get()) # deletion of record
        messagebox.showinfo("Date","Deleted Sucessfully!")
        Events_List_Box.delete(0,END)
        jab.destroy()
        conn.commit()
        conn.close()
        
    else:
        messagebox.showerror("Error","Please enter a valid no.")

#This function shows all the records present in our Event table
def records():
    global jab
    global query_label
    global Events_List_Box

    jab = Toplevel() # Creating a new window
    jab.title("Records list")
    jab.minsize(400,450)
    jab.resizable(False,False)
    jab.iconbitmap('calender.ico')

    conn = sqlite3.connect("Reminders_store.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM Event")
    records = c.fetchall()

    frame3 =Frame(jab, height=450,width=400,bg='light gray') #creating a frame
    frame3.place(x=0,y=0)
    
    print_record = ''
    for record in records:
        print_record += str(f"""{str(record[3])}){record[0]}
    """)+"\n"

    heading = Label(frame3,text='JABS REMINDER LISTS',font=("Helvetica",20,"bold"),width=24,bg="#BA0101",fg='white')
    heading.place(x=0,y=0,height=60)

    query_label = Label(frame3, text = print_record,bg = 'light gray', fg = "black" ,width=40,font=("Helvetica",12,))
    query_label.place(x=40,y=75)

    Events_List_Box = Entry(frame3, width=10)
    Events_List_Box.place(x=285,y=300,height=30)

    list_no = Label(frame3,text="Enter the Reminder List no:",font=("Helvetica",12,"bold"),bg='light gray')
    list_no.place(x=60, y=300,height=30)

    edit_btn = Button(frame3, text = "UPDATE",cursor='hand2',font=("Helvetica",12,), fg = "white",bg = "black",command= edit) #Buttons
    edit_btn.place(x=60,y=375)

    Delete_Button = Button(frame3,text ="DELETE",cursor='hand2',font=("Helvetica",12),fg = "white",bg ="black", command =delete)
    Delete_Button.place(x=275,y=375)

#creating a function to clear the entry box when the user clicks on it
def remove(Event):
    a=Entry_Box.get()
    if a=="Enter Your Event Here:":
        Entry_Box.delete(0, END)

options = [
    "January",
    "Feburary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

month = StringVar() #so that we can store string values
month.set(options[0])

frame=Frame(win, height=450,width=400,bg='light gray').place(x=0,y=0)

heading = Label(frame,text='JABS REMINDER',font=("Helvetica",20,"bold"),fg='white',width=24,bg="#BA0101")
heading.place(x=0,y=0,height=60)

Entry_Box = Entry(frame,width=40)
Entry_Box.place(x=60,y=80,height=40)
Entry_Box.insert(0,"Enter Your Event Here:")
Entry_Box.bind('<FocusIn>', remove) # calling the clear function

drop = OptionMenu(frame, month, *options) #creating a drop down menu
drop.config(font=("Helvetica",10,),cursor='hand2',)
drop.place(x=215,y=150,width=99,)

Month = Label(frame, text = "MONTH",font=("Helvetica",12,"bold"), bg = "LIGHT GRAY",fg='BLACK')
Month.place(x=100,y=155)

options=[]
for i in range(1,32):
    options.append(i)

day = IntVar() 
day.set(options[0])

 #conditions
if month.get() == "January":
    m = 1
elif month.get() == "Feburary":
    m = 2
elif month.get() == "March":
    m =3
elif month.get() == "April":
    m = 4
elif month.get() == "May":
    m = 5
elif month.get() == "June":
    m = 6
elif month.get() == "July":
    m = 7
elif month.get() == "Agust":
    m =8
elif month.get() == "September":
    m = 9
elif month.get() == "October":
    m =10
elif month.get() == "November":
    m = 11
else:
    m =12

Day = Label(frame, text = "DAY",font=("Helvetica",12,"bold"), bg = "black",fg='white')
Day.place(x=110,y=230)

drop2 = OptionMenu(frame,day,*options ) #drop down box for the days
drop2.config(font=("Helvetica",10),cursor='hand2',)
drop2.place(x=215,y=225,width=99)

Reminedr_list = Button(frame, text='REMINDER LIST',font=("Helvetica",12,'bold'),cursor='hand2',fg='white',border=0,bg='black', command = records)
Reminedr_list.place(x=140, y=320, height=40)

Add = Button(frame, text = "ADD",font=("Helvetica",12,'bold'),fg="WHITE",cursor='hand2',bg ="BLACK",border=0,width=5, command = subbmit)
Add.place(x=330,y=80, height=40)

Exit = Button(win,text = "EXIT",font=("Helvetica",12,'bold'), fg = "WHITE",cursor='hand2',bg = "BLACK" ,border=0,width=5, command=close)
Exit.place(x = 180, y = 400,height=40)

win.mainloop() #running an infinite loop until the user wants to exit