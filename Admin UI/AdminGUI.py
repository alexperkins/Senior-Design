from tkinter import Tk, Label, Button, W, scrolledtext
from SSH import getLog
import time
import threading
import logging
import os

class TextHandler(logging.Handler):

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(Tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(Tk.END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)


class AdminGUI:
    def __init__(self, master):
        self.master = master

        master.title('Honeypot Admin')
        master.option_add('*tearOff', 'FALSE')

        self.sysLog_button = Button(master, text="System Log", command=self.getSysLog)
        self.sysLog_button.grid()

        self.authLog_button = Button(master, text="Auth Log", command=self.getAuthLog)
        self.authLog_button.grid()

        self.userLog_button = Button(master, text="User Log", command=self.getUserLog)
        self.userLog_button.grid()

        self.logScroll = scrolledtext.ScrolledText(master,state="disabled", height=45,width=200)
        self.logScroll.grid(column=1, row=1, sticky='w', columnspan=10)
        self.text_handler = TextHandler(self.logScroll)


    def getSysLog(self):
        print("Getting syslog")
        remotePath = "/var/log/syslog"
        localPath = "C:\\Users\\Public\\Documents\\Honeypot Admin\\Sys Logs\\"
        logFileName = getLog(remotePath ,localPath, "sysLog")
        currFile = localPath + logFileName
        self.readLogFile(currFile)

    def getAuthLog(self):
        print("Getting authlog")
        remotePath = "/var/log/syslog"
        localPath = "C:\\Users\\Public\\Documents\\Honeypot Admin\\Auth Logs\\"
        logFileName = getLog(remotePath, localPath, "authLog")
        currFile = localPath + logFileName
        self.readLogFile(currFile)


    def getUserLog(self):
        print("Getting userlog")
        remotePath = "/var/log/syslog"
        localPath = "C:\\Users\\Public\\Documents\\Honeypot Admin\\Sys Logs\\"
        logFileName = getLog(remotePath, localPath, "sysLog")
        currFile = localPath + logFileName
        self.readLogFile(currFile)


    def readLogFile(self, logFilePath):
        logging.basicConfig(filename=logFilePath,level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.addHandler(self.text_handler)
        self.reader(logFilePath)

    def reader(self, currFile):
        file = open(currFile, 'r')
        for line in file:
            self.logScroll.insert("insert",line)

root = Tk()
my_gui = AdminGUI(root)
root.mainloop()
