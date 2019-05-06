#A loop that will activate once a picture is taken and uploaded#
#Good as of April 6, 2019 at 2:38pm#
#By: Justin Bennett#
import urllib.request as urlreq
import string
from ftplib import FTP_TLS


def RecievingCommand():
    rightCommand = False
    while not rightCommand:
        x = urlreq.urlopen('https://vulcuns-webserver.000webhostapp.com/Command.txt').read().decode()
        command = list(x.lower().split(" "))
        if 'sample' in command:
            command = 'sample'
            rightCommand = True
        elif 'moob' in command:
            command = 'moob'
            rightCommand = True
        elif 'immovable' in command:
            command = 'immovable'
            rightCommand = True
        elif 'movable' in command:
            command = 'movable'
            rightCommand = True
        else:
            pass
    return command
def DeleteTextFile():
    filename = 'test.txt'
    session = FTP_TLS('files.000webhost.com','vulcuns-webserver','AKPJJDT2lol')
    session.cwd('public_html')
    session.delete(filename)
    session.quit()
    
