import sys
import os
import time
import threading
import zmq
import numpy as np

from pi_client import ClientStreamer

connection_flag = False

def message_handler():

    global connection_flag
    global exit_signal

    connected = "connected"
    disconnected = "disconnected"
    
    print "message handler thread started"
    messaging_socket = zmq.Context().socket(zmq.SUB)
    messaging_socket.bind('tcp://*:5051')
    messaging_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
    
    while not exit_signal.is_set():
        try:
            incoming_message = messaging_socket.recv_string()
            print "received message: ", incoming_message
            if incoming_message == connected:
                connection_flag = True
                print "connected"
            elif incoming_message == disconnected:
                connection_flag = False
                print "disconnected"
        except:
            pass

    print "exiting messaging thread"
    return

            
def main(argv):

    global connection_flag
    global exit_signal
    
    print "main thread started"
    client = ClientStreamer()
    print "client object"
    client.connect_streaming_socket("18.214.123.134", "5050")
    print "connected socket"
    client.start_camera()
    print "camera initialized"

    # start stream
    for frame in client.camera.capture_continuous(client.rawCapture, format="bgr",
                                                  use_video_port=True):
        
        try:
            if exit_signal.is_set():
                print "camera shutdown"
                break
            if connection_flag == True:
                client.encode_and_send_image(frame)
            client.rawCapture.truncate(0)
            
        except:
            print "camera exception"
            break
        
    print "exiting main thread"
    return
        
if __name__ == "__main__":

    exit_signal = threading.Event()

    main_t = threading.Thread(target=main, args=(sys.argv[:],))
    message_handler_t = threading.Thread(target=message_handler)
    
    message_handler_t.daemon = True
    
    main_t.start()
    message_handler_t.start()
    
    try:
        while not exit_signal.is_set():
            # let the program breath
            time.sleep(0.2)
    
    except KeyboardInterrupt:
        print "exit signal set"
        exit_signal.set()

    print "exit script"


    
    
        
    
