#import modules
from cgitb import text
from tkinter import *
from tkinter import LEFT, Y, Canvas, Frame, Label, ttk
from turtle import width
from typing import Text
from tkcalendar import Calendar 
from PIL import ImageTk, Image
import datetime as dt
from time import strftime
import datetime
import os
from Quotes import a
import sqlite3
from tkinter import *
import datetime
import time
from tkinter import messagebox
import sqlite3


#creating window 
win = Tk()
win.title("JABS CALENDER DASHBOARD")   #WINDOW TITLE
win.geometry("1280x720")               #WINDOW SIZE
theme=('helvetica',12,'bold')          #FONT
theme_a=('helvetica',17,'bold')        #FONT

#bg image
bg=  PhotoImage(file= 'JABSdash_logo.png')
bg_lbl = Label(win, image=bg)
bg_lbl.place(x=0)

# frame
FrameOne=Frame(win, height=595,width=390,bg="#BA0101").place(x=50,y=45)

FrameTwo = Frame(win, height=200,width=300,bg="#BA0101").place(x=80,y=80)

# MESSAGE BOX
Quotes = Message(FrameTwo, text ="Quotes of the day :\n\n"+a, font =('helvetica',12,'bold',"italic"),width=315, bg = "White",relief=GROOVE)
Quotes.place(x = 88, y= 310,height=135)

#COUNT DOWN

conn = sqlite3.connect("jabs.db")
c = conn.cursor()
c.execute("SELECT * FROM users") #getting the info of the active user
records = c.fetchall()
for record in records:
    if record[6] == 1:
        Dob = record[3]
        
        conn.commit()
        conn.close()
        break
    else:
        pass

dob = str(Dob) #converting the DOB to string

print(dob)

#breaking down the DOB into months, days and year
if len(dob) == 6:
    a = dob[0]
    b = dob[2]
    c = dob[4] + dob[5]
elif len(dob) == 7:
    if dob[1] == "/":
        a = dob[0]
        b = dob[2] + dob[3]
        c = "20" + dob[5] + dob[6]
    else:
        a = dob[0] + dob[1]
        b =dob[3]
        c = "20" + dob[5] + dob[6]
elif len(dob) == 8:
    a = dob[0] + dob[1]
    b = dob[3] + dob[4]
    c = "20" + dob[6] + dob[7]

#checking if the birthday of this year hass passed or not
ok = int(time.strftime('%m'))
month = int(a)
day = int(b)
if ok >= month :
    year = 2023
else:
    year = 2022

Birth = datetime.date(year,month,day)-datetime.date.today()
Ok = str(Birth)
Birth2 = Ok.replace('0:00:00','')
Birth3 = Birth2.replace('day,','')
Birth0 = Birth3.replace('days,','')

#condition to decide the remaning days for the birthday
if Birth0 == "":
    Birth0 = 0
    messagebox.showinfo("Birthday","Happy Birthday ! Have a healty and happy year.") #message box to wish the user
    
elif int(Birth0) < 0:
    Birth = datetime.date(2023,7,21)-datetime.date.today()
    Ok = str(Birth)
    Birth2 = Ok.replace('0:00:00','')
    Birth3 = Birth2.replace('days,','')
    Birth0 = Birth3.replace('days,','')
else:
    pass

My_Labe1 = Label(FrameTwo, bg = "#BA0101",relief=GROOVE,border=0)
My_Labe1.place(x=88,y=250,height=50)

#This function contains the Birthday label
def Timer():
    My_Labe1.config(text = f"""{Birth0}Days Left for Your Birthday""",font = ("Helvetica",15,"bold"),fg='#ffff00')
    My_Labe1.after(1000,Timer)

#calling Timer
Timer()

# DEFINE FUNCTION FOR GREETING
def greeting():
    global name
    currentTime = datetime.datetime.now()
    currentTime.hour
    conn = sqlite3.connect("jabs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    records = c.fetchall()
    for record in records:
        print(record)
        if record[6] == 1:
            name = record[0]
            
            conn.commit()
            conn.close()
            break
        else:
            pass
    

    if currentTime.hour < 12:
        label = Label(FrameTwo, text=f"Good Morning, {name}",font= ('helvetica',17,),fg='WHITE',bg="#BA0101")
        label.place(x=85, y=95)
    elif 12 <= currentTime.hour < 18:
        label = Label(FrameTwo, text=f"Good Afternoon, {name}",font=('helvetica',17,),fg='WHITE',bg="#BA0101")
        label.place(x=85, y=95)
    else:
        label = Label(FrameTwo, text=f"Good Evening, {name}",font= ('helvetica',17,),fg='WHITE',bg="#BA0101")
        label.place(x=85, y=95)
greeting()

date = dt.datetime.now()
# Create Label to display the Date
label1 = Label(FrameTwo, text=f"{date:%A}", font=('helvetica',25,'bold'),fg='WHITE',bg="#BA0101")  #for day of a week
label1.place(x=85,y=125)
label = Label(FrameTwo, text=f"{date: %B %d, %Y}", font=('helvetica',25,'bold'),fg='WHITE',bg="#BA0101")   #for month day and year
label.place(x=75,y=170)

# TIME 
def time():
    string = strftime(' %H-%M-%S %p')
    lbl.config(text = string,fg='WHITE')
    lbl.after(1000, time)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(win, font = ('helvetica',11,'bold'),bg="#BA0101")
lbl.place(x=80,y=215)
time()
  
def note():
    os.system('python newnotes.py')

def user():
    win.destroy()
    os.system('python Profile.py')
    

def reminder():
    os.system('python Reminder_2.py')

profile=Button(FrameOne,text="User",font=theme,bg='white',cursor='hand2',background='light gray',relief=FLAT,command=user)
profile.place(x=380,y=55,height=40)

note_btn=Button(FrameOne,text="Notes",font=theme,width=20,bg='white',cursor='hand2',background='light gray',border=5,relief=FLAT,command=note)
note_btn.place(x=140,y=480,height=50)

reminder_btn=Button(FrameOne,text="Reminder",font=theme,width=20,cursor='hand2',bg='light gray',relief=FLAT, command=reminder)
reminder_btn.place(x=140,y=560,height=50)

#Calendar
cal = Calendar( font="Ariel 14",selectmode='day').grid(row=0,column=1,padx=525,pady=130,ipadx=170,ipady=130)

#Calendar : Cover of Unnecessary no.
cal = Label(cal, text=" ",height=27,width=3,bg='#b3b3b3').place(x=530,y=200)

mainloop()
