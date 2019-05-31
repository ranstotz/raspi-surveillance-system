#!/usr/bin/python
import os
import sys
from message_sender import MessageSender

def main(argv):

    client = MessageSender()
    client.connect_messaging_socket("18.214.123.134", 5050)
    client.send_message("test message")
    
    return


if __name__ == "__main__":
    main(sys.argv[:])
    
