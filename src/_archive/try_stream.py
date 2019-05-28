import sys
import os
import time
import threading
import zmq
import numpy as np

from pi_client import ClientStreamer
from message_receiver import MessageReceiver

connection_flag = False
messaging_socket = zmq.Context().socket(zmq.SUB)
messaging_socket.bind('tcp://*:5051')
#messaging_socket.bind('tcp://18.214.123.134:5051')
messaging_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

while True:
    try:
        incoming_message = messaging_socket.recv_string()
        print incoming_message
    except:
        pass

def messaging_thread():

    global connection_flag
    messaging_socket = zmq.Context().socket(zmq.SUB)
    messaging_socket.connect('tcp://18.214.123.134:5051')
    messaging_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

    listening = False
    incoming_message = ''
    while True:
        
        if listening == False:
            print "listening..."
            listening = True

        try:
            incoming_message = messaging_socket.recv_string()
            print incoming_message
            if incoming_message != '':
                print "incoming message is: ", incoming_message
            if incoming_message == "connected":
                connection_flag = True
                print "message received, connection: ", connection_flag
            elif incoming_message == "disconnected":
                # note that it doesn't make it here, server fails to send message
                connection_flag = False
                print "message received, connection: ", connection_flag
    
        except:
            print "exception thrown in message thread"
            pass

            
def main(argv):
    global connection_flag
    print "starting script"
    client = ClientStreamer()

    message_thread = threading.Thread(target=messaging_thread)
    message_thread.start()
    
    client.connect_streaming_socket("18.214.123.134", "5050")
    client.start_camera()
    print "camera initialized"
    # start stream
    for frame in client.camera.capture_continuous(client.rawCapture, format="bgr",
                                                  use_video_port=True):
        
        
        try:

            #if connection_flag == True:
            client.encode_and_send_image(frame)
            client.rawCapture.truncate(0)
            
        except KeyboardInterrupt:
            client.camera.release()
            message_receiver.close_connection()
            message_thread.join()
            break
    return
        
if __name__ == "__main__":
    main(sys.argv[:])
