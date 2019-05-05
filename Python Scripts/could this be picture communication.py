#Takes Picture#
from ftplib import FTP_TLS
from picamera import PiCamera
from time import sleep

def TakePicture():
    camera = PiCamera()
    filename = 'PhotoCommand.jpeg' #name of file
#f ".jpeg" in filename:
    #camera.capture("/home/pi/CSCI-121/Webserver_jazz/" + filename)
#else:
   #camera.start_recording("/home/pi/CSCI-121/Webserver_jazz/" + filename)
    #sleep(5)
    #camera.stop_recording()

#Moves file to directory on webserver#

#transfers file to the webserver#

session = FTP_TLS('files.000webhost.com','vulcuns-webserver','AKPJJDT2lol') #ftp for webserver
#login#
file = open(filename, 'rb') #open the data from the file
session.cwd('public_html/images') #directory of images
session.storbinary('STOR ' + filename, file) #stores the file in current directory
file.close() #closes the file
session.quit() #logs out of webserver ftp connection
