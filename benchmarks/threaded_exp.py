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
import threading


def write_files(cv):
    global shared_buffer

    condition.acquire()
    while len(shared_buffer) == 0:
        condition.wait()
    cv2.imwrite(shared_buffer[0][0], shared_buffer[0][1])
    shared_buffer.pop()
    print "wrote image"
    condition.release()

    
# main function
def main(cv, argv):

    global shared_buffer
    
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

    # initialize file-writing thread
    fw_t = threading.Thread(target=write_files)
    
    file_name = ""
    frameCounter = 0
    # capture frames from camera
    while fps._numFrames < args["frames"]:
        frame = vs.read()
        fps.update()
        print "length buf: ", len(shared_buffer)
        file_name = "output/test" + str(frameCounter) + ".jpg"
        condition.acquire()
        shared_buffer.append((file_name, frame))
        condition.notify()
        condition.release()
        frameCounter += 1

    fps.stop()

    print "frames: ", fps._numFrames
    print "time:   ", fps.elapsed()
    print "FPS:    ", fps.fps()
        
    return


if __name__ == "__main__":
    shared_buffer = []
    condition = threading.Condition()
    main_thread = threading.Thread(target=main, args=(condition, sys.argv[:],))
    writer_thread = threading.Thread(target=write_files, args=(condition,))

    main_thread.start()
    writer_thread.start()
    



