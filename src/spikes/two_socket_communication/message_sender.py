import sys
import socket
import time

class MessageSender(object):
    ''' Sends text messages through web socket '''


    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_messaging_socket(self, ip, port):
        self.sock.connect((ip, port))

    def send_message(self, message):
        while True:
            try:
                self.sock.sendall(message)
                time.sleep(1)
            except KeyboardInterrupt:
                print "keyboard interrupt, yo"
                self.conn.close()
                sys.exit()
            
