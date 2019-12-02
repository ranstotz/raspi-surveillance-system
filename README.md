# Surveillance Project Data
## Author: Ryan Anstotz

Note: stream-video.py is the driver script.

## Summary
The goal of this project is to use a Raspberry Pi 3+ to record a surveillance
video feed. Then the Pi will send the video via HTTP stream to a separate
server. This server will store the video in 24-hour increments and provide
accessibility to the stream via a password-protected website. The program will
for the Pi will be written in Python using the OpenCV library for video
recording and storage and an HTTP library for streaming. 

## Next Steps
   - Create zmq socket on new port (prob 5051) and open respective firewalls.
   - Lightsail will be pub, Pi sub.
   - Create Pi script to wait for signal to begin/end stream and add logic in
     pi_client.py class (pi) to stop the video.
     - Need to ensure start method works with stop method.
   - Make sure that no packets are sent when stream stops. Read up on zmq.
   - On Lightsail side, need to be able to handle clicks on website to:
     1.) View the stream (this should always be available.
     2.) Record the stream. If recording started, should be able to stop,
     	 then download if wanted.
     3.) When new recording started, all previous recording data should be wiped.
     	 - May need to Spawn a new process for this.
	 - Also, need to create a new folder with a timestamp so that new data
	   isn't wiped. 
     	 

## Progress
Use https://pyzmq.readthedocs.io/en/latest/api/zmq.html to poll the server
and ensure a connection is made before sending the stream. Add the logic
so that the Pi doesn't auto stream everything. No need to be streaming
when the camera is not requested by the server. 


## Additional Data
Threaded video code in "benchmarks" directory. Increased FPS to 30 fps, however,
bottleneck with I/O. So this was kept as only an experiment. 



Thread the stream for increased FPS. Bottleneck at approx 14-15 FPS without streaming.
       - See: https://www.pyimagesearch.com/2015/12/28/increasing-raspberry-pi-fps-with-python-and-opencv/
       - Should try to manually thread some code, instead of using a library. 

Server receives approx. 7 FPS which is probably a socket capacity issue, or a second threading problem.



===========================================================================
## *** new_effort reference ***:
https://raspberrypi.stackexchange.com/questions/72308/how-to-stream-video-via-socket-using-opencv-and-picamera

## A few References:

