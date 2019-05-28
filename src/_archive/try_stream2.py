import sys
import os
import threading
import time
import zmq
import numpy as np

from pi_client import ClientStreamer

def main(argv):

    print "main thread started"
    # streaming video
    client = ClientStreamer()
    client.connect_streaming_socket("18.214.123.134", "5050")
    client.start_camera()
    client.begin_stream()
    return

def message_handler():
    print "message handler thread started"
    messaging_socket = zmq.Context().socket(zmq.SUB)
    messaging_socket.bind('tcp://*:5051')
    #messaging_socket.bind('tcp://18.214.123.134:5051')
    messaging_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
    
    while True:
        try:
            incoming_message = messaging_socket.recv_string()
            print incoming_message
        except:
            sys.exit()
    return

if __name__ == "__main__":
    main_t = threading.Thread(target=main, args=(sys.argv[:],))
    message_handler_t = threading.Thread(target=message_handler)

    message_handler_t.daemon = True
    
    main_t.start()
    message_handler_t.start()
