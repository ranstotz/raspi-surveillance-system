import cv2
import zmq
import base64
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

context = zmq.Context()
footage_socket = context. socket(zmq.PUB)
footage_socket.connect('tcp://localhost:5555')

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr",
                                       use_video_port=True):
    try:
        #grabbed, frame = camera.read()
        #fame = cv2.resize(frame, (640, 480))
        image = frame.array

        encoded, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)
        rawCapture.truncate(0)
        
    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break

    
        
