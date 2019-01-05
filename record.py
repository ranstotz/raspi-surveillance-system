# Surveillance Project
# Author: Ryan Anstotz
# =================================================================================

# import necessary packages
import os
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# main function
def main(argv):

    # initialize camera
    camera = PiCamera()
    print "Initialized camera..."
    rawCapture = PiRGBArray(camera)

    # allow the camera to warm-up
    time.sleep(0.1)

    # grab an image from the camera, smile!
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array 
    
    # display image on screen and wait for a keypress
    cv2.imshow("Image", image)
    print "Displayed image..."
    cv2.waitKey(0)
    
    # return from main
    return


if __name__ == "__main__":
    main(sys.argv[:])

# end of file

