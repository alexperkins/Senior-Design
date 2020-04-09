import os
import paramiko
from datetime import datetime
import Authorization

def getLog(sourcePath,destinationPath,fileString):
    currentDate = datetime.today().strftime('%Y-%m-%d')
    newLogFile = fileString + currentDate + '.log'
    localPath = destinationPath + newLogFile   #destination path
    remotepath = sourcePath    #source path
    ssh = paramiko.SSHClient()
    ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
    Authorization.genWindow()
    host = Authorization.host
    user = Authorization.user
    passwd = Authorization.passwd
    ssh.connect(hostname=host, username=user, password=passwd)
    sftp = ssh.open_sftp()

    serverFile = sftp.open(remotepath,mode='r',bufsize=-1)
    currentDate = datetime.today().strftime('%Y-%m-%d')
    f = open(localPath,'w')

    for line in serverFile:
        f.write(line)

    sftp.close()
    ssh.close()
    return newLogFile
