# Surveillance Project Data
## Author: Ryan Anstotz

The goal of this project is to use a Raspberry Pi 3+ to record a surveillance
video feed. Then the Pi will send the video via HTTP stream to a separate
server. This server will store the video in 24-hour increments and provide
accessibility to the stream via a password-protected website. The program will
for the Pi will be written in Python using the OpenCV library for video
recording and storage and an HTTP library for streaming. 

## Progress
Created successful stream. Appears to be sending full video through socket in
new_effort. Next step is to put the scripts into classes, then import them
into Flask to serve on the website. After that, make it password protected,
and have a nice intereface!

- Put config files in /etc/ for port/ip.
~
~
~
===========================================================================
## *** new_effort reference ***:
https://raspberrypi.stackexchange.com/questions/72308/how-to-stream-video-via-socket-using-opencv-and-picamera

## A few References:

Router IP:
https://stackoverflow.com/questions/19246103/socket-errorerrno-99-cannot-assign-requested-address-and-namespace-in-python

Verizon router ref:
https://forums.verizon.com/t5/Fios-Internet/Help-with-IP-Cameras-to-port-forward-Verizon-router/td-p/835700


https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

https://stackoverflow.com/questions/30988033/sending-live-video-over-network-in-python-opencv 
