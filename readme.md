# Surveillance Project Data
## Author: Ryan Anstotz

The goal of this project is to use a Raspberry Pi 3+ to record a surveillance
video feed. Then the Pi will send the video via HTTP stream to a separate
server. This server will store the video in 24 hour increments and provide
accessibility to the stream via a password-protected website. The program will
for the Pi will be written in Python using the OpenCV library for video
recording and storage and an HTTP library for streaming. 

## A few References:
https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

https://stackoverflow.com/questions/30988033/sending-live-video-over-network-in-python-opencv 

## OLD DATA

This is for regular use of camera over localhost.

Reference Website:
https://tutorials-raspberrypi.com/raspberry-pi-security-camera-livestream-setup/

How to start service:
sudo service motion start

To stop:
sudo service motion stop
Data is stored as jpegs to the /home/pi/Monitor directory and streamed over
the localhost. 


