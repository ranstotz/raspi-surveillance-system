import sys
import os
import time
import threading
import socket

from pi_client import ClientStreamer
from message_receiver import MessageReceiver

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_flag = False

def messaging_thread():
    global sock
    global connection_flag
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    
    sock.bind(('', 5051))
    while True:

        sock.listen(1)
        conn, address = sock.accept()
        try:
            incoming_message = conn.recv(1024)
            if incoming_message == "connected":
                connection_flag = True
                print "message received, connection: ", connection_flag
            elif incoming_message == "disconnected":
                # note that it doesn't make it here, server fails to send message
                connection_flag = False
                print "message received, connection: ", connection_flag
                conn.close()
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
    '''
    message_receiver.connect_messaging_socket('', 5051)
    ''' 
    client.start_camera()
    print "camera initialized"
    # start stream
    for frame in client.camera.capture_continuous(client.rawCapture, format="bgr",
                                                  use_video_port=True):
        
        
        try:

            if connection_flag == True:
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
