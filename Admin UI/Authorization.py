from tkinter import *
from functools import partial

host = ""
user = ""
passwd = ""

def validateLogin(hostname,username, password):
    host = hostname
    user = username
    passwd = password

def genWindow():
    tkWindow = Tk()
    tkWindow.geometry('200x150')
    tkWindow.title('Honeypot Admin Login')

    hostnameLabel = Label(tkWindow, text="Host Name").grid(row=0, column=0)
    hostname = StringVar()
    hostnameEntry = Entry(tkWindow, textvariable=hostname).grid(row=0, column=1)

    usernameLabel = Label(tkWindow, text="User Name").grid(row=1, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=1, column=1)

    passwordLabel = Label(tkWindow,text="Password").grid(row=2, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=2, column=1)

    validateLogin(hostnameEntry, usernameEntry, passwordEntry)

    #login button
    loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

    tkWindow.mainloop()