# Surveillance Project
# File: server_cv.py
# Author: Ryan Anstotz
# Description:
#  Receives stream over socket, stores stream
# =================================================================================

# import necessary packages
import os
import sys
import numpy as np
import socket
import pickle
import struct
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import time 
import cv2
 
# import functions/classes
from config import *

# main function
def main(argv):

    
    # set host and port for socket
    host = '71.175.97.72'
    port = 5050
    
    # socket parameters
    script_type = "server"
    data_file = argv[1]
    HOST, PORT = parse_config(data_file, script_type)

    print HOST, PORT, type(HOST), type(PORT)
    print host, port, type(host), type(port)

    
    # initialize socket connections
    print "Creating socket..."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket created."

    # bind socket
    s.bind((HOST, PORT))
    print "Socket bind complete."
    s.listen(10)
    print "Socket now listening."

    # accept connection
    conn, addr = s.accept()
    print "Socket connected to IP:", addr[0]
    
    # data prep. 'L' stands for unsigned long
    data = ""
    payload_size = struct.calcsize("L")

    # a test flag that will print something upon success
    accepted_flag = False
    
    # accept data continuously
    while (1):

        # get and process the payload
        while len(data) < payload_size:
            data += conn.recv(4096)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        # load image
        image = pickle.loads(frame_data)

        if accepted_flag == False:
            accepted_flag = True
            print "*** the code appears to have worked ***"
            print " this is the first row of the image array "
            print image[0]
        '''
        # display the stream
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF

        # if 'q' key pressed, break from loop
        if key == ord("q"):
            break
        '''
        
    # return from main
    return

# execute 
if __name__ == "__main__":
    main(sys.argv[:])

# end of file
