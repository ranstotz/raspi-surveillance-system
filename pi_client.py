import cv2
import zmq
import base64
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

class clientStreamer(object):
    ''' clientStreamer '''

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        print "Initiallizing context and socket."
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.PUB)
        print "Context and socket initialized. \nBinding to port."
        #self.footage_socket.connect('tcp://localhost:5050')    # local testing
        self.footage_socket.connect('tcp://18.214.123.134:5050')
        print "Port initialized.\n"
        self.camera = ""
        self.rawCapture = ""
        
    def start_camera(self):
        print "Initializing camera..."
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
        time.sleep(0.1)    # Warm up camera
        print "Camera initialized."
    
    def begin_stream(self):
        
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr",
                                               use_video_port=True):
            try:
                image = frame.array
                encoded, buffer = cv2.imencode('.jpg', image)
                jpg_as_text = base64.b64encode(buffer)
                self.footage_socket.send(jpg_as_text)
                self.rawCapture.truncate(0)
                
            except KeyboardInterrupt:
                self.camera.release()
                cv2.destroyAllWindows()
                break



