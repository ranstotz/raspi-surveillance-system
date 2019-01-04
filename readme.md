Surveillance Project Data

Reference Website:
https://tutorials-raspberrypi.com/raspberry-pi-security-camera-livestream-setup/

How to start service:
sudo service motion start

To stop:
sudo service motion stop

To restart:
sudo service motion restart

Data is stored as jpegs to the /home/pi/Monitor directory and streamed over
the localhost (192.168.1.231:8081).

Next step, send stream of images to Lightsail server. Then if requested, serve
them live (slightly delayed), to the website (password protected). May need
to build software for this. But once images saved on cloud, accessing them is
next.
