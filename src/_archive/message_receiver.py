import sys
import socket
import time

class MessageReceiver(object):

    def __init__(self):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = ""
        self.address = ""
        
    def connect_messaging_socket(self, ip, port):
        self.sock.bind((ip, port))
        self.sock.listen(1)
        self.conn, self.address = self.sock.accept()


    def close_connection(self):
        self.conn.close()

    def get_message(self):
        message = self.conn.recv(1024)
        return message

        
    def print_message_on_loop(self):
        while True:
            try:
                message = self.conn.recv(1024)
                print message
            except KeyboardInterrupt:
                self.conn.close()
                sys.exit()
                
