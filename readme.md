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

Next goal is to send data to web server, store frames in 24-hour increments
and allow live streaming on website when requested.

Currently have a "working" model. Socket is created from server to client.
Some sort of data is transmitted, however the data appears to be
coming in slowly from first glance. Also, the struct 32 vs 64 bit was
resolved by changing the "L" to "=L".

Next, the images will need to be saved, then rsync'd to my local
machine for examination. More debugging required.

Put config files in /etc/ for port/ip.

*** new_effort reference ***:
https://raspberrypi.stackexchange.com/questions/72308/how-to-stream-video-via-socket-using-opencv-and-picamera

## A few References:

Router IP:
https://stackoverflow.com/questions/19246103/socket-errorerrno-99-cannot-assign-requested-address-and-namespace-in-python

Verizon router ref:
https://forums.verizon.com/t5/Fios-Internet/Help-with-IP-Cameras-to-port-forward-Verizon-router/td-p/835700


https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

https://stackoverflow.com/questions/30988033/sending-live-video-over-network-in-python-opencv 
