# Surveillance Project Data
## Author: Ryan Anstotz

Note: stream-video.py is the driver script.

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

## Next steps
Thread the stream for increased FPS. Bottleneck at approx 14-15 FPS without streaming.
       - See: https://www.pyimagesearch.com/2015/12/28/increasing-raspberry-pi-fps-with-python-and-opencv/
       - Should try to manually thread some code, instead of using a library. 

Server receives approx. 7 FPS which is probably a socket capacity issue, or a second threading problem. 

===========================================================================
## *** new_effort reference ***:
https://raspberrypi.stackexchange.com/questions/72308/how-to-stream-video-via-socket-using-opencv-and-picamera

## A few References:

