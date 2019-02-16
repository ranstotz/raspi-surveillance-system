import cv2
import zmq
import base64
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

class clientStreamer(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.footage_socket = ""

    def initialize_client(self):
        print "Initiallizing context and socket."
        context = zmq.Context()
        footage_socket = context.socket(zmq.PUB)
        print type(footage_socket)
        print "Context and socket initialized. \nBinding to port."
        #footage_socket.connect('tcp://localhost:5555')
        footage_socket.connect('tcp://18.214.123.134:5050')
        print "Port initialized.\n"

    def start_camera(self):
        print "Initializing camera."
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
        time.sleep(0.1) # Warm up camera
        print "Camera initialized."
    
    def begin_stream(self):
        
        for frame in camera.capture_continuous(rawCapture, format="bgr",
                                               use_video_port=True):
            try:
                image = frame.array
                encoded, buffer = cv2.imencode('.jpg', image)
                jpg_as_text = base64.b64encode(buffer)
                footage_socket.send(jpg_as_text)
                rawCapture.truncate(0)
                
            except KeyboardInterrupt:
                camera.release()
                cv2.destroyAllWindows()
                break



