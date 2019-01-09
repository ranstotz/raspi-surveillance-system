# Surveillance Project
# File: client_cv.py
# Author: Ryan Anstotz
# Description:
#  Records video to send to a server
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

    # initialize socket connections
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname("localhost")
    clientsocket.connect((host, 8089))
    print "Socket initialized."

    # initialize camera
    camera = PiCamera()
    print "Initialized camera."
    
    # set params
    height = 640
    width = 480
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    
    # warm up camera
    time.sleep(0.2)
    
    # capture frames from camera
    for frame in camera.capture_continuous(rawCapture, format="bgr",
                                           use_video_port=True):
        # grab raw Numpy array representing the image, then
        # initialize timestamp and text
        image = frame.array

        # serialize data
        data = pickle.dumps(image)

        # send data over socket in binary form
        clientsocket.sendall(struct.pack("L", len(data))+data)
                
        '''
        # not doing this since that will be server-side
        # show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        '''
        
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

    # return from main
    return

# execute 
if __name__ == "__main__":
    main(sys.argv[:])

# end of file

