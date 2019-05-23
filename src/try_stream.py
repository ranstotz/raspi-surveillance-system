import sys
import os
import time
import threading

from pi_client import ClientStreamer
from message_receiver import MessageReceiver

connection_flag = False

def messaging_thread(message_receiver):
    message_receiver.connect_messaging_socket('', 5051)
    while True:
        incoming_message = message_receiver.get_message()
        if incoming_message == "hello there":
            print "message received"
        
    
def main(argv):
    print "starting script"
    client = ClientStreamer()
    message_receiver = MessageReceiver()

    message_thread = threading.Thread(target=messaging_thread, args=(message_receiver,))
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
            client.encode_and_send_image(frame)
            
        except KeyboardInterrupt:
            client.camera.release()
            message_receiver.close_connection()
            break
        
if __name__ == "__main__":
    main(sys.argv[:])
