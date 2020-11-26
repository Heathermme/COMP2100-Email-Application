# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:59:49 2020

@author: volge
"""

from tkinter import *
import smtplib

#Main Screen Init
master = Tk()
master.title = ('Email Application')
master.minsize(width = 200, height = 200)
master.config(bg = 'white')

#Functions
def send():
    try: 
        username = temp_username.get()
        password = temp_password.get()
        to       = temp_receiver.get()
        subject  = temp_subject.get()
        body     = temp_body.get()
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notif.config(text="All fields required", fg="red")
            return
        else:
            finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
            server   = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username,to,finalMessage)
            notif.config(text="Email has been sent successfully", fg="green")
    except:
        notif.config(text="Error sending email", fg="red")


def reset():
  usernameEntry.delete(0,'end')
  passwordEntry.delete(0,'end')
  receiverEntry.delete(0,'end')
  subjectEntry.delete(0,'end')
  bodyEntry.delete(0,'end')

#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject  = StringVar()
temp_body     = StringVar()

#Labels
title = Label(master, text="Python Email Application", font=('Calibri',40))
title.pack()
detail = Label(master, text="Enter Information Into the Fields Below", font=('Calibri',11))
detail.pack()
enteraddress = Label(master, text="Email", font=('Calibri', 15))
enteraddress.pack()
usernameEntry = Entry(master, width = 40, textvariable = temp_username)
usernameEntry.pack()
enterpassword = Label(master, text="Password", font=('Calibri', 15))
enterpassword.pack()
passwordEntry = Entry(master, show="*", width = 40, textvariable = temp_password)
passwordEntry.pack()
enterreceiver = Label(master, text="Receiver Email", font=('Calibri', 15))
enterreceiver.pack()
receiverEntry  = Entry(master, width = 40, textvariable = temp_receiver)
receiverEntry.pack()
entersubject = Label(master, text="Subject", font=('Calibri', 15))
entersubject.pack()
subjectEntry  = Entry(master, width = 40, textvariable = temp_subject)
subjectEntry.pack()
entermessage = Label(master, text="Body", font=('Calibri', 15))
entermessage.pack()
bodyEntry = Entry(master, width = 40, textvariable = temp_body)
bodyEntry.pack()
notif = Label(master, text="", font=('Calibri', 15),fg="red")
notif.pack()


#Buttons
button1 = Button(master, text = "Send", command = send)
button1.pack()
button2 = Button(master, text = "Reset", command = reset)
button2.pack()

#Mainloop
master.mainloop()