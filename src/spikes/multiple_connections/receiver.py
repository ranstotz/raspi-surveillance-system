''' script listens to multiple connections from publishers and accepts messages '''

import sys
import zmq
import time
import numpy as np

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

