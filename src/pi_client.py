import cv2
import numpy as np
import zmq
import base64
from picamera.array import PiRGBArray
from picamera import PiCamera
import time


class Streamer(object):
    """ 
    Object to stream frames from a Raspberry Pi camera over the wire (TCP)
    in an encoded JPEG. Camera information can be modified in start_camera 
    method. 
    """

    def __init__(self):
        """ Prepares socket for stream. """

        self.footage_socket = zmq.Context().socket(zmq.PUB)
        self.camera = ""
        self.rawCapture = ""

    def connect_streaming_socket(self, ip, port):
        """ Creates connection with port at specified ip. Ensure firewalls 
            are compatible. """

        connection_address = 'tcp://' + ip + ':' + port
        self.footage_socket.connect(connection_address)

    def start_camera(self):
        """ Initializes camera settings. """

        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
        time.sleep(0.1)    # Warm up camera

    def encode_and_send_image(self, frame):
        """ Encodes the images as a JPEG, then with base64. Then sends the image. """
        image = frame.array
        encoded, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer)
        self.footage_socket.send(jpg_as_text)

    def begin_stream(self):
        """ Method for debugging purposes. Captures and streams in a single method. """

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
                sys.exit()
                break
