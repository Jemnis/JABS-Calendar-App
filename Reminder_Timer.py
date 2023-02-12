#importing imp modulws
from tkinter import *
import datetime
import time
from tkinter import messagebox
import sqlite3

#creting a window
win =  Toplevel()
global Dob
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


My_Labe1 = Label(win,text = "")
My_Labe1.grid(row = 0, column=0)



#This function contains the Birthday label
def Timer():
    My_Labe1.config(text = f"""{Birth0}Days Left
    """,font = ("Helvetica",18,"bold"))
    My_Labe1.after(1000,Timer)

#calling Timer
Timer()
win.mainloop()



            



