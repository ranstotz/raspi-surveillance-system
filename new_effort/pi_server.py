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
        
    def initialize_server(self):
        print "Initiallizing context and socket."
        context = zmq.Context()
        footage_socket = context.socket(zmq.SUB)
        print type(footage_socket)
        print "Context and socket initialized. \nBinding to port."
        footage_socket.bind('tcp://*:5050')
        footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
        print "Port initialized.\n"

    def capture_stream(self):
        connectionFlag = False
        while True:
            try:
                frame = footage_socket.recv_string()
                if connectionFlag == False:
                    print "Connection made. Now streaming.\n"
                    connectionFlag = True
                img = base64.b64decode(frame)
                npimg = np.fromstring(img, dtype=np.uint8)
                source = cv2.imdecode(npimg, 1)
                #cv2.imshow("Stream", source)
                cv2.waitKey(1)
                print "captured data"
                
            except KeyboardInterrupt:
                cv2.destroyAllWindows()
                break
    

    
