#text communication script for Pi-Car#

import urllib.request as urlreq
recieve_command = False
while not recieve_command:
    command = urlreq.urlopen('https://vulcuns-webserver.000webhostapp.com/test.txt').read()
    string = command.decode('utf-8')
    if string != 'This is not the moob-\n':
        print('Wrong command')
    else:
        print('Correct Command')
    recieve_command = True

