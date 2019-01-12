# Surveillance Project Data
## Author: Ryan Anstotz

The goal of this project is to use a Raspberry Pi 3+ to record a surveillance
video feed. Then the Pi will send the video via HTTP stream to a separate
server. This server will store the video in 24-hour increments and provide
accessibility to the stream via a password-protected website. The program will
for the Pi will be written in Python using the OpenCV library for video
recording and storage and an HTTP library for streaming. 

## Progress
Camera currently streams frames via socket over the localhost. A client
and server script are used for this implementation.

Immediate goal is to test json config file. Then work with ports on router.

Next goal is to send data to web server, store frames in 24-hour increments
and allow live streaming on website when requested.



## A few References:
https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

https://stackoverflow.com/questions/30988033/sending-live-video-over-network-in-python-opencv 
