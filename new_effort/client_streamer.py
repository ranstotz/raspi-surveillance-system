import cv2
import zmq
import base64

context = zmq.Context()
footage_socket = context. socket(zmq.PUB)
footage_socket.connect('tcp://localhost:8080')

# Init camera 
camera = cv2.VideoCapture(0)

while True:
    try:
        grabbed, frame = camera.read()
        frame = cv2.resize(frame, (640, 480))
        encoded, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break

    
        
