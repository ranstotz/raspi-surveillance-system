import sys
import os

from pi_client import clientStreamer

def main(argv):

    client = clientStreamer()
    
    client.connect_streaming_socket("18.214.123.134", "5050")
    '''
    client.connect_messaging_socket("*", "5051")
    message = ""
    while True:
    message = client.receive_message()
    print message
    '''
    client.start_camera()
    client.begin_stream()

if __name__ == "__main__":
    main(sys.argv[:])
