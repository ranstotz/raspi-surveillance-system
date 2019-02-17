import cv2
import numpy as np
import zmq
import base64
import time

class serverViewer(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.footage_socket = ""
        
        print "Initiallizing context and socket."
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.SUB)
        print "Context and socket initialized. \nBinding to port."
        self.footage_socket.bind('tcp://*:5050')
        self.footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
        print "Port initialized.\n"

    def capture_stream(self):
        connectionFlag = False
        while True:
            try:
                frame = self.footage_socket.recv_string()
                if connectionFlag == False:
                    print "Connection made. Now streaming.\n"
                    connectionFlag = True
                img = base64.b64decode(frame)
                npimg = np.fromstring(img, dtype=np.uint8)
                source = cv2.imdecode(npimg, 1)
                cv2.imshow("Stream", source)
                cv2.waitKey(1)
                print "captured data"
                
            except KeyboardInterrupt:
                cv2.destroyAllWindows()
                break
    
    def get_frame(self):
        try:
            frame = self.footage_socket.recv_string()
            img = base64.b64decode(frame)
            npimg = np.fromstring(img, dtype=np.uint8)
            source = cv2.imdecode(npimg, 1)
            temp = open("stream.jpg", 'wb+')
            if source:
                cv2.imwrite("stream.jpg", source)
            return source
        
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break
        
    
