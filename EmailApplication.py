# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:59:49 2020

@author: volge
"""

from tkinter import *
import smtplib
import webbrowser

#Main Screen Initialize (creating gui window)
master = Tk()
master.title = ('Email Application')
master.minsize(width = 200, height = 200)
master.config(bg = "#699768")

#Send Email Function (creating main variables, establishing smtp connection)
def send():
    try: 
        username = t_username.get()
        password = t_password.get()
        receiver = t_receiver.get()
        subject  = t_subject.get()
        body     = t_body.get()
        if username=="" or password=="" or receiver=="" or subject=="" or body=="":
            notif.config(text="All fields required", fg="red")
            return
        else:
            finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
            server   = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username,receiver,finalMessage)
            notif.config(text="Email has been sent successfully", fg="#3f5a3f")
    except:
        notif.config(text="Error sending email", fg="red")
#Reset Function (Setting entries to empty)
def reset():
  usernameEntry.delete(0,'end')
  passwordEntry.delete(0,'end')
  receiverEntry.delete(0,'end')
  subjectEntry.delete(0,'end')
  bodyEntry.delete(0,'end')
  
#Warning Function (Opens a website when warning is clicked) 
def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")

#Storage 
t_username = StringVar()
t_password = StringVar()
t_receiver = StringVar()
t_subject  = StringVar()
t_body     = StringVar()

#Interface (labels, entries, and buttons)
title = Label(master, text="Python Gmail Application",borderwidth=2, relief="ridge",fg="white", bg="#699768", font=('Trebuchet MS',40,'bold'))
title.pack()
warning = Label(master, text="Click Here to Change Email Setting (Needed for App)", fg="#253525",bg="#699768",font=('Trebuchet MS',15,'bold'), cursor="hand2")
warning.bind("<Button-1>", setup)
warning.pack()
detail = Label(master, text="Enter Your Information:",fg="white", bg="#699768", font=('Trebuchet MS',15))
detail.pack()
enteraddress = Label(master, text="Sender Email",fg="white", bg="#699768", font=('Trebuchet MS', 20))
enteraddress.pack()
usernameEntry = Entry(master, width = 30,textvariable = t_username,borderwidth=2, relief="ridge", font=('Trebuchet MS', 13))
usernameEntry.pack()
enterpassword = Label(master, text="Password",fg="white", bg="#699768", font=('Trebuchet MS', 20))
enterpassword.pack()
passwordEntry = Entry(master, show="*", width = 30, textvariable = t_password,borderwidth=2, relief="ridge", font=('Trebuchet MS', 13))
passwordEntry.pack()
enterreceiver = Label(master, text="Receiver Email",fg="white", bg="#699768", font=('Trebuchet MS', 20))
enterreceiver.pack()
receiverEntry  = Entry(master, width = 30, textvariable = t_receiver,borderwidth=2, relief="ridge", font=('Trebuchet MS', 13))
receiverEntry.pack()
entersubject = Label(master, text="Subject",fg="white", bg="#699768", font=('Trebuchet MS', 20))
entersubject.pack()
subjectEntry  = Entry(master, width = 30, textvariable = t_subject,borderwidth=2, relief="ridge", font=('Trebuchet MS', 13))
subjectEntry.pack()
entermessage = Label(master, text="Body",fg="white", bg="#699768", font=('Trebuchet MS', 20))
entermessage.pack()
bodyEntry = Entry(master,width = 30, textvariable = t_body,borderwidth=2, relief="ridge",font=('Trebuchet MS', 20))
bodyEntry.pack()
notif = Label(master, text="", font=('Trebuchet MS', 20),fg="red",bg="#699768")
notif.pack()

button1 = Button(master, text = " Send ", font=('Trebuchet MS', 15), command = send)
button1.pack()
button2 = Button(master, text = "Reset", font=('Trebuchet MS', 15), command = reset)
button2.pack()

#Mainloop
master.mainloop()