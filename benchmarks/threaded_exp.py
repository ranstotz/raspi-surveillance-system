# Surveillance Project
# File: video_capture_exp.py
# Author: Ryan Anstotz
# Description:
#  Benchmark speed of video capture framerate
# =================================================================================

# import necessary packages
import os
import sys
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import time 
import cv2
import argparse

# main function
def main(argv):

    # get args
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--frames", type=int, default=100)
    args = vars(ap.parse_args())
    
    print "Initializing threaded video... "
    '''
    # initialize camera
    camera = PiCamera()
    height = 640
    width = 480
    camera.resolution = (height, width)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))
    stream = camera.capture_continuous(rawCapture, format="bgr",
                                       use_video_port=True)
    '''
    print "starting stream object" 
    vs = PiVideoStream((1280, 720), 30).start()
    fps = FPS().start()
    
    # warm up camera
    time.sleep(0.8)
    print "Starting threaded video capture... "
    

    frameCounter = 0
    # capture frames from camera
    while fps._numFrames < args["frames"]:
        frame = vs.read()
        fps.update()
        file_name = "output/test" + str(frameCounter) + ".jpg"
        cv2.imwrite(file_name, frame)
        frameCounter += 1
    fps.stop()

    print "frames: ", fps._numFrames
    print "time:   ", fps.elapsed()
    print "FPS:    ", fps.fps()
        
    return


if __name__ == "__main__":
    main(sys.argv[:])


