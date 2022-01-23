from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import re
import sqlite3

mydb = sqlite3.connect('busbookingsystem.db')
c = mydb.cursor()

class Application():
        
    def __init__(self, windows):
        self.windows = windows

        self.left = Frame(windows, width=950, height=740, bg='alice blue')
        self.left.pack(side=LEFT)

        self.title = Label(self.left, text="Bus Booking System", font=(
            'forte 40 bold'), fg='black', bg='light steel blue')
        self.title.place(x=220, y=15)

        imgfile = ImageTk.PhotoImage(Image.open("bus1.gif"))
        img = Label(self.left,image=imgfile)
        img.image = imgfile
        img.place(x=22, y=100)

        self.submit = Button(self.left, text="Add Bus", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.addbus)
        self.submit.place(x=790, y=120)

        self.submit = Button(self.left, text="Search Bus", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.searchbus)
        self.submit.place(x=790, y=180)

        self.submit = Button(self.left, text="Exit", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.exit)
        self.submit.place(x=790, y=665)

        self.submit = Button(self.left, text="Bookings", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.status)
        self.submit.place(x=790, y=240)

    def addbus(self):

        self.left = Frame(self.left, width=950, height=740, bg='alice blue')
        self.left.pack(side=LEFT)

        imgfile = ImageTk.PhotoImage(Image.open("addbus.jpg"))
        img = Label(self.left,image=imgfile)
        img.image = imgfile
        img.place(x=180, y=100)

        self.title = Label(self.left, text="Bus Booking System", font=(
            'forte 40 bold'), fg='black', bg='light steel blue')
        self.title.place(x=200, y=15)

        self.n = Label(self.left, text="Full Name", font=(
            'Mistral 18 bold'), fg='black', bg='lavender')
        self.n.place(x=240, y=140)


        self.c = Label(self.left, text="Contact No.", font=(
            'Mistral 18 bold'), fg='black', bg='lavender')
        self.c.place(x=240, y=180)


        self.add = Label(self.left, text="Address", font=(
            'Mistral 18 bold'), fg='black', bg='lavender')
        self.add.place(x=240, y=220)

        self.nametextentry = Entry(self.left, width=30)
        self.nametextentry.place(x=450, y=147)

        self.contacttextentry = Entry(self.left, width=30)
        self.contacttextentry.place(x=450, y=187)

        self.addresstextentry = Entry(self.left, width=30)
        self.addresstextentry.place(x=450, y=227)

        self.submit = Button(self.left, text="Add Details", width=9, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.adddetails)
        self.submit.place(x=270, y=265)

        self.submit = Button(self.left, text="Exit", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.exit)
        self.submit.place(x=500, y=265)

    def adddetails(self):

        self.value1 = self.nametextentry.get()
        self.value2 = self.contacttextentry.get()
        self.value3 = self.addresstextentry.get()

        if self.value1 == '' or self.value2 == '' or self.value3 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes!")

        else:
            try:
                val = type(int(self.value2))
            except:
                tkinter.messagebox.showinfo("Warning","Invalid Input Type!")

            else:
                self.opr = Label(self.left, text="Operator", font=(
                'Mistral 18 bold'), fg='black', bg='lavender')
                self.opr.place(x=240, y=330)

                self.type = Label(self.left, text="Bus Type", font=(
                    'Mistral 18 bold'), fg='black', bg='lavender')
                self.type.place(x=240, y=370)

                self.frm = Label(self.left, text="From", font=(
                    'Mistral 18 bold'), fg='black', bg='lavender')
                self.frm.place(x=240, y=410)

                self.to = Label(self.left, text="To", font=(
                    'Mistral 18 bold'), fg='black', bg='lavender')
                self.to.place(x=240, y=450)

                self.date = Label(self.left, text="Date", font=(
                    'Mistral 18 bold'), fg='black', bg='lavender')
                self.date.place(x=240, y=490)

                self.dept = Label(self.left, text="Departure Time", font=(
                    'Mistral 18 bold'), fg='black', bg='lavender')
                self.dept.place(x=240, y=530)

                self.arr = Label(self.left, text="Arrival Time", font=(
                    'Mistral 18 bold'), fg='black', bg='lavender')
                self.arr.place(x=240, y=570)

                self.fare = Label(self.left, text="Fare", font=(
                    'Mistral 18 bold'), fg='black', bg='lavender')
                self.fare.place(x=240, y=610)

                self.seats = Label(self.left, text="Seats", font=(
                    'Mistral 18 bold'), fg='black', bg='lavender')
                self.seats.place(x=240, y=650)

                self.oprtextentry = Entry(self.left, width=30)
                self.oprtextentry.place(x=450, y=333)

                self.typetextentry = Entry(self.left, width=30)
                self.typetextentry.place(x=450, y=373)

                self.frmtextentry = Entry(self.left, width=30)
                self.frmtextentry.place(x=450, y=413)

                self.totextentry = Entry(self.left, width=30)
                self.totextentry.place(x=450, y=453)

                self.datetextentry = Entry(self.left, width=30)
                self.datetextentry.place(x=450, y=493)

                self.depttextentry = Entry(self.left, width=30)
                self.depttextentry.place(x=450, y=533)

                self.arrtextentry = Entry(self.left, width=30)
                self.arrtextentry.place(x=450, y=573)

                self.faretextentry = Entry(self.left, width=30)
                self.faretextentry.place(x=450, y=613)

                self.seatstextentry = Entry(self.left, width=30)
                self.seatstextentry.place(x=450, y=653)

                self.submit = Button(self.left, text="Save", width=8, font=("Jokerman"),
                                     height=1, bg='AntiqueWhite1', command=self.add_appointment)
                self.submit.place(x=660, y=630)

                self.submit = Button(self.left, text="Home", width=8, font=("Jokerman"),
                                     height=1, bg='AntiqueWhite1', command=self.home)
                self.submit.place(x=660, y=570)

    def add_appointment(self):

        self.value1 = self.nametextentry.get()
        self.value2 = self.contacttextentry.get()
        self.value3 = self.addresstextentry.get()
        self.value4 = self.oprtextentry.get()
        self.value5 = self.typetextentry.get()
        self.value6 = self.frmtextentry.get()
        self.value7 = self.totextentry.get()
        self.value8 = self.datetextentry.get()
        self.value9 = self.depttextentry.get()
        self.value10 = self.arrtextentry.get()
        self.value11 = self.faretextentry.get()
        self.value12 = self.seatstextentry.get()


        if self.value4 == '' or self.value5 == '' or self.value6 == '' or self.value7 == '' or self.value8 == '' or self.value9 == '' or self.value10 == '' or self.value11 == '' or self.value12 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes!")

        elif not self.dateformat(self.value8):
            tkinter.messagebox.showinfo("Warning", "Check Date Format!")

        else:
            try:
                val = type(int(self.value11))
                val1 = type(int(self.value12))
            except:
                tkinter.messagebox.showinfo("Warning","Invalid Input Type!")

            else:
                try:           
                    sql = '''INSERT INTO appointments (name, contact, address, operator, type, frm, t, dat, departure, arrival, fare, seats) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                    val = (self.value1, self.value2, self.value3, self.value4, self.value5, self.value6, self.value7, self.value8, self.value9, self.value10, self.value11, self.value12)
                    c.execute(sql, val)
                    mydb.commit()
                    tkinter.messagebox.showinfo("Success", "Details Added Successfully!")

                except:
                    tkinter.messagebox.showinfo("Error","Contact Already Exists!")

    def home(self):

        self.left = Frame(self.left, width=950, height=740, bg='alice blue')
        self.left.pack(side=LEFT)

        self.title = Label(self.left, text="Bus Booking System", font=(
            'forte 40 bold'), fg='black', bg='light steel blue')
        self.title.place(x=220, y=15)

        imgfile = ImageTk.PhotoImage(Image.open("bus1.gif"))
        img = Label(self.left,image=imgfile)
        img.image = imgfile
        img.place(x=22, y=100)

        self.submit = Button(self.left, text="Add Bus", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.addbus)
        self.submit.place(x=790, y=120)

        self.submit = Button(self.left, text="Search Bus", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.searchbus)
        self.submit.place(x=790, y=180)

        self.submit = Button(self.left, text="Exit", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.exit)
        self.submit.place(x=790, y=665)

        self.submit = Button(self.left, text="Bookings", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.status)
        self.submit.place(x=790, y=240)

    def searchbus(self):

        self.left = Frame(self.left, width=950, height=740, bg='alice blue')
        self.left.pack(side=LEFT)

        imgfile = ImageTk.PhotoImage(Image.open("searchbus.jpg"))
        img = Label(self.left,image=imgfile)
        img.image = imgfile
        img.place(x=50, y=90)

        self.title = Label(self.left, text="Bus Booking System", font=(
            'forte 40 bold'), fg='black', bg='light steel blue')
        self.title.place(x=220, y=15)

        self.head = Label(self.left, text="Get Your Ride!", font=(
            'Broadway 33 bold'), fg='LemonChiffon3', bg="white")
        self.head.place(x=530, y=480)

        self.bustype = Label(self.left, text="Bus Type", font=(
            'Mistral 18 bold'), fg='black', bg='lavender')
        self.bustype.place(x=100, y=140)

        self.frm = Label(self.left, text="From", font=(
            'Mistral 18 bold'), fg='black', bg='lavender')
        self.frm.place(x=100, y=180)

        self.to = Label(self.left, text="To", font=(
            'Mistral 18 bold'), fg='black', bg='lavender')
        self.to.place(x=100, y=220)

        self.date = Label(self.left, text="Date", font=(
            'Mistral 18 bold'), fg='black', bg='lavender')
        self.date.place(x=100, y=260)

        optionlist = ["AC", "Non-AC", "AC Sleeper", "Non-AC Sleeper", "All Types"]

        self.variable = StringVar(self.left)
        self.variable.set(optionlist[4])
        

        self.bustypetextentry = OptionMenu(self.left, self.variable, *optionlist)
        self.bustypetextentry.place(x=240, y=145)
        

        self.frmtextentry = Entry(self.left, width=30)
        self.frmtextentry.place(x=240, y=190)

        self.totextentry = Entry(self.left, width=30)
        self.totextentry.place(x=240, y=230)

        self.datetextentry = Entry(self.left, width=30)
        self.datetextentry.place(x=240, y=270)

        self.submit = Button(self.left, text="Home", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.home)
        self.submit.place(x=112, y=320)

        self.submit = Button(self.left, text="Search", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.find)
        self.submit.place(x=250, y=320)

        self.submit = Button(self.left, text="Exit", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.exit)
        self.submit.place(x=760, y=570)

    def find(self):

        self.value13 = self.variable.get()
        self.value14 = self.frmtextentry.get()
        self.value15 = self.totextentry.get()
        self.value16 = self.datetextentry.get()

        if self.value14 == '' or self.value15 == '' or self.value16 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes!")

        elif self.value14 == self.value15:
            tkinter.messagebox.showinfo("Warning", "Please Enter Different Destination/Source")

        elif not self.dateformat(self.value16):
            tkinter.messagebox.showinfo("Warning", "Check date format!")

        else:

            self.left = Frame(self.left, width=950, height=740, bg='alice blue')
            self.left.pack(side=LEFT)

            imgfile = ImageTk.PhotoImage(Image.open("findbus.jpg"))
            img = Label(self.left,image=imgfile)
            img.image = imgfile
            img.place(x=25, y=100)

            self.title = Label(self.left, text="Bus Booking System", font=('forte 40 bold'), fg='black', bg='light steel blue')
            self.title.place(x=220, y=15)

            self.opr = Label(self.left, text="Operator", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.opr.place(x=30, y=410)

            self.type = Label(self.left, text="Bus Type", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.type.place(x=135, y=410)

            self.frm = Label(self.left, text="From", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.frm.place(x=250, y=410)

            self.to = Label(self.left, text="To", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.to.place(x=358, y=410)

            self.date = Label(self.left, text="Date", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.date.place(x=440, y=410)

            self.dept = Label(self.left, text="Departure", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.dept.place(x=505, y=410)

            self.arr = Label(self.left, text="Arrival", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.arr.place(x=618, y=410)

            self.fare = Label(self.left, text="Fare", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.fare.place(x=703, y=410)

            self.seats = Label(self.left, text="Seat(s)", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.seats.place(x=768, y=410)

            self.seats = Label(self.left, text="Select", font=(
                'georgia 13 bold'), fg='black', bg='lavender')
            self.seats.place(x=855, y=410)

            if self.value13 == "All Types":
                sql = "SELECT * FROM appointments WHERE frm=? AND t=? AND dat=?"
                c.execute(sql, (self.value14, self.value15, self.value16))
                self.r = c.fetchall()
 
            else:
                sql = '''SELECT * FROM appointments WHERE frm=? AND t=? AND dat=? AND type=?'''
                c.execute(sql, (self.value14, self.value15, self.value16, self.value13))
                self.r = c.fetchall()

            if not self.r:

                tkinter.messagebox.showinfo("Oops", "No Buses Found!")
                self.searchbus()

            else:

                self.axis = 450
                i = 1
                self.v = IntVar()
                
                for self.row in self.r:
                    self.name = self.row[0]
                    self.contact = self.row[1]
                    self.address = self.row[2]
                    self.operator = self.row[3]
                    self.type = self.row[4]
                    self.frm = self.row[5]
                    self.to = self.row[6]
                    self.date = self.row[7]
                    self.dept = self.row[8]
                    self.arr = self.row[9]
                    self.fare = self.row[10]
                    self.seats = self.row[11]

                    self.opr = Label(self.left, text=self.operator, font=(
                    'Consolas 10'), fg='black')
                    self.opr.place(x=30, y=self.axis)

                    self.type = Label(self.left, text=self.type, font=(
                        'Consolas 10'), fg='black')
                    self.type.place(x=130, y=self.axis)

                    self.frm = Label(self.left, text=self.frm, font=(
                        'Consolas 10'), fg='black')
                    self.frm.place(x=237, y=self.axis)

                    self.to = Label(self.left, text=self.to, font=(
                        'Consolas 10'), fg='black')
                    self.to.place(x=340, y=self.axis)

                    self.date = Label(self.left, text=self.date, font=(
                        'Consolas 10'), fg='black')
                    self.date.place(x=429, y=self.axis)

                    self.dept = Label(self.left, text=self.dept, font=(
                        'Consolas 10'), fg='black')
                    self.dept.place(x=534, y=self.axis)

                    self.arr = Label(self.left, text=self.arr, font=(
                        'Consolas 10'), fg='black')
                    self.arr.place(x=622, y=self.axis)

                    self.fare = Label(self.left, text="INR "+str(self.fare), font=(
                        'Consolas 10'), fg='black')
                    self.fare.place(x=697, y=self.axis)

                    self.seats = Label(self.left, text=self.seats, font=(
                        'Consolas 10'), fg='black')
                    self.seats.place(x=797, y=self.axis)

                    self.rb = Radiobutton(self.left, variable=self.v, value=i, command=self.book)
                    self.rb.place(x=870, y=self.axis)

                    self.axis = self.axis + 30
                    i = i + 1

                self.submit = Button(self.left, text="Home", width=8, font=("Jokerman"),
                                 height=1, bg='AntiqueWhite1', command=self.home)
                self.submit.place(x=790, y=110)

                self.submit = Button(self.left, text="Exit", width=8, font=("Jokerman"),
                                 height=1, bg='AntiqueWhite1', command=self.exit)
                self.submit.place(x=790, y=170)

    def book(self):
        
        self.selection = self.v.get()
        self.submit = Button(self.left, text="Book", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.details)
        self.submit.place(x=827, y=self.axis+10)


    def details(self):

        self.right=Frame(self.left,width=380, height=740,bg='peach puff')
        self.right.pack(side=RIGHT)

        self.left = Frame(self.left, width=570, height=740, bg='alice blue')
        self.left.pack(side=LEFT)
        
        self.bookdetails = Label(self.right, text="Booking Details", font=('Broadway 23 bold'), fg='black', bg='gold')
        self.bookdetails.place(x=50, y=15)

        imgfile = ImageTk.PhotoImage(Image.open("info.jpg"))
        img = Label(self.left,image=imgfile)
        img.image = imgfile
        img.place(x=100, y=110)

        self.title = Label(self.left, text="Bus Booking System", font=('forte 40 bold'), fg='black', bg='light steel blue')
        self.title.place(x=40, y=15)

        self.passenger = Label(self.left, text="Passenger Details", font=('Mistral 20 bold'), fg='black')
        self.passenger.place(x=180, y=440)

        self.passname = Label(self.left, text="Name", font=('georgia 12 bold'), fg='black', bg='lavender')
        self.passname.place(x=100, y=500)

        self.type = Label(self.left, text="Contact No.", font=('georgia 12 bold'), fg='black', bg='lavender')
        self.type.place(x=100, y=540)

        self.seat = Label(self.left, text="No. of seat(s)", font=('georgia 12 bold'), fg='black', bg='lavender')
        self.seat.place(x=100, y=580)

        self.passnametextentry = Entry(self.left, width=20)
        self.passnametextentry.place(x=273, y=503)

        self.phonetextentry = Entry(self.left, width=20)
        self.phonetextentry.place(x=273, y=543)

        self.seattextentry = Entry(self.left, width=5)
        self.seattextentry.place(x=310, y=583)

        
        self.submit = Button(self.left, text="Book Now", width=8,height=1,  font=("Jokerman"), bg='AntiqueWhite1', command=self.info)
        self.submit.place(x=282, y=615)

        self.submit = Button(self.left, text="Home", width=8,height=1,  font=("Jokerman"), bg='AntiqueWhite1', command=self.home1)
        self.submit.place(x=160, y=615)

    def info(self):

        self.value21 = self.passnametextentry.get()
        self.value22 = self.phonetextentry.get()
        self.value23 = self.seattextentry.get()
                
        if self.value21=='' or self.value22=='' or self.value23=='':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes!")
        else:

            try:
                val = type(int(self.value22))
                val1 = type(int(self.value23))
            except:
                tkinter.messagebox.showinfo("Warning","Invalid Input Type!")

            else:
            
                row2=self.r[self.selection-1]

                if int(row2[11])-int(self.value23)>=0 and int(self.value23) > 0:

                    try:
                
                        sql = '''INSERT INTO details (passname, phone, seat) VALUES(?, ?, ?)'''
                        val = (self.value21, self.value22, self.value23)
                        c.execute(sql, val)
                        mydb.commit()

                    except:
                        tkinter.messagebox.showinfo("Error","Booking not confirmed!")

                    else:

                        tkinter.messagebox.showinfo("Success","Booking Confirmed")

                        sql1 = '''UPDATE appointments SET seats=? WHERE contact=?'''
                        val1 = (int(row2[11])-int(self.value23), row2[1])
                        c.execute(sql1, val1)
                        mydb.commit()

                        self.dpassname = Label(self.right, text="Passenger Name:   "+self.value21, font=('georgia 10'), fg='black', bg='white')
                        self.dpassname.place(x=15, y=105)

                        self.dtype = Label(self.right, text="Passenger Contact No.:   "+self.value22, font=('georgia 10'), fg='black', bg='white')
                        self.dtype.place(x=15, y=135)
                        self.dseat = Label(self.right, text="No. of seat(s) reserved:   "+self.value23, font=('georgia 10'), fg='black', bg='white')
                        self.dseat.place(x=15, y=165)
                        self.dname = Label(self.right, text="Operator Full Name:   "+row2[0], font=('georgia 10'), fg='black', bg='white')
                        self.dname.place(x=15, y=195)
                        self.dcontact = Label(self.right, text="Operator Contact No.:   "+str(row2[1]), font=('georgia 10'), fg='black', bg='white')
                        self.dcontact.place(x=15, y=225)
                        self.daddress = Label(self.right, text="Operator Address:   "+row2[2], font=('georgia 10'), fg='black', bg='white')
                        self.daddress.place(x=15, y=255)
                        self.doperator = Label(self.right, text="Operator:   "+row2[3], font=('georgia 10'), fg='black', bg='white')
                        self.doperator.place(x=15, y=285)
                        self.dtype = Label(self.right, text="Bus Type:   "+row2[4], font=('georgia 10'), fg='black', bg='white')
                        self.dtype.place(x=15, y=315)
                        self.dfrm = Label(self.right, text="From:   "+row2[5], font=('georgia 10'), fg='black', bg='white')
                        self.dfrm.place(x=15, y=345)
                        self.dto = Label(self.right, text="To:   "+row2[6], font=('georgia 10'), fg='black', bg='white')
                        self.dto.place(x=15, y=375)
                        self.ddate = Label(self.right, text="Date Of Journey:   "+row2[7], font=('georgia 10'), fg='black', bg='white')
                        self.ddate.place(x=15, y=405)
                        self.ddept = Label(self.right, text="Departure Time:   "+row2[8], font=('georgia 10'), fg='black', bg='white')
                        self.ddept.place(x=15, y=435)
                        self.darr = Label(self.right, text="Arrival Time:   "+row2[9], font=('georgia 10'), fg='black', bg='white')
                        self.darr.place(x=15, y=465)
                        self.dfare = Label(self.right, text="Total Fare:   INR "+str(int(row2[10])*int(self.value23)), font=('georgia 10'), fg='black', bg='white')
                        self.dfare.place(x=15, y=495)

                        sql = '''INSERT INTO status (pname,pcontact, pseats, ocontact, oper, btype, fr, too, doj, dtime, atime, pfare) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                        val = (self.value21, int(self.value22), self.value23, row2[1], row2[3], row2[4], row2[5], row2[6], row2[7], row2[8], row2[9], str(int(row2[10])*int(self.value23)))
                        c.execute(sql, val)
                        mydb.commit()

                        self.submit = Button(self.left, text="Exit", width=8,  font=("Jokerman"), height=1, bg='AntiqueWhite1', command=self.exit)
                        self.submit.place(x=278, y=675)
                    
                else:

                    tkinter.messagebox.showinfo("Alert","Seats not available!")

    def home1(self):

        self.right=Frame(self.right,width=0, height=0)
        self.right.pack(side=RIGHT)

        self.left = Frame(self.left, width=950, height=740, bg='alice blue')
        self.left.pack(side=LEFT)

        self.title = Label(self.left, text="Bus Booking System", font=(
            'forte 40 bold'), fg='black', bg='light steel blue')
        self.title.place(x=220, y=15)

        imgfile = ImageTk.PhotoImage(Image.open("bus1.gif"))
        img = Label(self.left,image=imgfile)
        img.image = imgfile
        img.place(x=22, y=100)

        self.submit = Button(self.left, text="Add Bus", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.addbus)
        self.submit.place(x=790, y=120)

        self.submit = Button(self.left, text="Search Bus", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.searchbus)
        self.submit.place(x=790, y=180)

        self.submit = Button(self.left, text="Exit", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.exit)
        self.submit.place(x=790, y=665)

        self.submit = Button(self.left, text="Bookings", width=8, font=("Jokerman"),
                             height=1, bg='AntiqueWhite1', command=self.status)
        self.submit.place(x=790, y=240)

    def status(self):

        self.left = Frame(self.left, width=950, height=740, bg='alice blue')
        self.left.pack(side=LEFT)

        self.title = Label(self.left, text="Bus Booking System", font=('forte 40 bold'), fg='black', bg='light steel blue')
        self.title.place(x=220, y=15)

        imgfile = ImageTk.PhotoImage(Image.open("status.jpg"))
        img = Label(self.left,image=imgfile)
        img.image = imgfile
        img.place(x=140, y=110)

        self.passenger = Label(self.left, text="Check Booking Status", font=('Mistral 24 bold'), fg='black')
        self.passenger.place(x=580, y=118)

        self.number = Label(self.left, text="Passenger's registered number", font=('georgia 12 bold'), fg='black', bg='lavender')
        self.number.place(x=573, y=198)

        self.conttextentry = Entry(self.left, width=20)
        self.conttextentry.place(x=638, y=241)

        self.submit = Button(self.left, text="Home", width=8, font=("Jokerman"),height=1, bg='AntiqueWhite1', command=self.home)
        self.submit.place(x=597, y=295)

        self.submit = Button(self.left, text="Check", width=8, font=("Jokerman"),height=1, bg='AntiqueWhite1', command=self.check)
        self.submit.place(x=718, y=295)

    def check(self):

        self.value25 = (self.conttextentry.get(),)

        if self.value25 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up The Box!")

        else:
            try:
                val = type(str(self.value25))
            except:
                tkinter.messagebox.showinfo("Warning","Invalid Input Type!")

            else:

                c.execute('SELECT * FROM status WHERE pcontact=?',self.value25)
                self.r = c.fetchall()

                if not self.r:

                    tkinter.messagebox.showinfo("Oops", "No Bookings Found!")
                    self.status()

                else:

                    self.opr = Label(self.left, text="Passenger Name", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.opr.place(x=5, y=410)

                    self.frm = Label(self.left, text="Seat(s)", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.frm.place(x=122, y=410)

                    self.date = Label(self.left, text="Operator Contact", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.date.place(x=178, y=410)

                    self.arr = Label(self.left, text="Operator", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.arr.place(x=308, y=410)

                    self.fare = Label(self.left, text="Bus Type", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.fare.place(x=400, y=410)

                    self.seats = Label(self.left, text="From", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.seats.place(x=487, y=410)

                    self.seats = Label(self.left, text="To", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.seats.place(x=578, y=410)

                    self.seats = Label(self.left, text="Journey", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.seats.place(x=651, y=410)

                    self.seats = Label(self.left, text="Departure", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.seats.place(x=722, y=410)

                    self.seats = Label(self.left, text="Arrival", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.seats.place(x=804, y=410)

                    self.seats = Label(self.left, text="Total Fare", font=('georgia 8 bold'), fg='black', bg='lavender')
                    self.seats.place(x=868, y=410)

                    self.axis = 450
                    
                    for self.row in self.r:
                        self.name = self.row[0]
                        self.seat = self.row[2]
                        self.contact = self.row[3]
                        self.operator = self.row[4]
                        self.type = self.row[5]
                        self.frm = self.row[6]
                        self.to = self.row[7]
                        self.date = self.row[8]
                        self.dept = self.row[9]
                        self.arr = self.row[10]
                        self.fare = self.row[11]

                        self.nam = Label(self.left, text=self.name, font=(
                        'Consolas 10'), fg='black')
                        self.nam.place(x=12, y=self.axis)

                        self.pseat = Label(self.left, text=self.seat, font=(
                            'Consolas 10'), fg='black')
                        self.pseat.place(x=136, y=self.axis)

                        self.phone = Label(self.left, text=self.contact, font=(
                            'Consolas 10'), fg='black')
                        self.phone.place(x=198, y=self.axis)

                        self.opr = Label(self.left, text=self.operator, font=(
                            'Consolas 10'), fg='black')
                        self.opr.place(x=280, y=self.axis)

                        self.typ = Label(self.left, text=self.type, font=(
                            'Consolas 10'), fg='black')
                        self.typ.place(x=378, y=self.axis)

                        self.fom = Label(self.left, text=self.frm, font=(
                            'Consolas 10'), fg='black')
                        self.fom.place(x=483, y=self.axis)

                        self.t = Label(self.left, text=self.to, font=(
                            'Consolas 10'), fg='black')
                        self.t.place(x=575, y=self.axis)

                        self.dat = Label(self.left, text=self.date, font=(
                            'Consolas 10'), fg='black')
                        self.dat.place(x=645, y=self.axis)

                        self.dep = Label(self.left, text=self.dept, font=(
                            'Consolas 10'), fg='black')
                        self.dep.place(x=730, y=self.axis)

                        self.arrv = Label(self.left, text=self.arr, font=(
                            'Consolas 10'), fg='black')
                        self.arrv.place(x=800, y=self.axis)

                        self.pfare = Label(self.left, text="INR "+str(self.fare), font=(
                            'Consolas 10'), fg='black')
                        self.pfare.place(x=873, y=self.axis)

                        self.axis = self.axis + 30

                    self.submit = Button(self.left, text="Exit", width=8, font=("Jokerman"),height=1, bg='AntiqueWhite1', command=self.exit)
                    self.submit.place(x=855, y=self.axis+10)

        
    def dateformat(self, a):
        
            pattern = r'(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])'
            match = re.search(pattern, a)
            if match:
                return True
            else:
                match1 = False
                match = False
                return False

    def exit(self):

        self.windows.destroy()
            
root = Tk()
b = Application(root)
root.title('Bus Booking System')
root.geometry("950x740")
root.resizable(False, False)
root.mainloop()
