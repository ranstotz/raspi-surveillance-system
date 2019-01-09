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
from picamera.array import PiRGBArray
from picamera import PiCamera
import time 
import cv2
 
# main function
def main(argv):

    # set host and port
    HOST = ''
    PORT = 8089
    
    # initialize socket connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "socket created"

    s.bind((HOST, PORT))
    print "Socket bind complete."
    s.listen(10)
    print "Socket now listening."

    conn, addr = s.accept()

    # data prep
    data = ""
    payload_size = struct.calcsize("L")
    
    # accept data
    while True:

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

        # show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF

        # if 'q' key pressed, break from loop
        if key == ord("q"):
            break
    
    # return from main
    return

# execute 
if __name__ == "__main__":
    main(sys.argv[:])

# end of file

