import cv2
import numpy as np
import zmq
import base64
from picamera.array import PiRGBArray
from picamera import PiCamera
import time


class Streamer(object):
    ''' Streamer class '''

    def __init__(self):

        self.footage_socket = zmq.Context().socket(zmq.PUB)
        self.camera = ""
        self.rawCapture = ""

    def connect_streaming_socket(self, ip, port):
        connection_address = 'tcp://' + ip + ':' + port
        self.footage_socket.connect(connection_address)

    def start_camera(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
        time.sleep(0.1)    # Warm up camera

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
                sys.exit()
                break

    def encode_and_send_image(self, frame):
        ''' this is to make capture_continuous for-loop in outside function. '''
        image = frame.array
        encoded, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer)
        self.footage_socket.send(jpg_as_text)
