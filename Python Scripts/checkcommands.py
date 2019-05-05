#A loop that will activate once a picture is taken and uploaded#
#Good as of April 6, 2019 at 2:38pm#
import urllib.request as urlreq
import string
from ftplib import FTP_TLS


def RecievingCommand():
    rightCommand = False
    while not rightCommand:
        command = urlreq.urlopen('https://vulcuns-webserver.000webhostapp.com/Command.txt').read().decode()
        if command.lower() == 'this is the sample':
            print('good job')
            rightCommand = True
           #DeleteTextFile()
        elif command.lower() == 'this is the moob':
            CommandList.append(command)
            print('get the hell outta here')
            rightCommand = True
            #DeleteTextFile()
        else:
            pass
    return command.lower()
def DeleteTextFile():
    filename = 'Command.txt'
    session = FTP_TLS('files.000webhost.com','vulcuns-webserver','AKPJJDT2lol')
    session.cwd('public_html')
    session.delete(filename)
    session.quit()
    
