import sys
import os

from pi_client import ClientStreamer

def main(argv):

    # streaming video
    client = ClientStreamer()
    client.connect_streaming_socket("18.214.123.134", "5050")
    client.start_camera()
    client.begin_stream()

if __name__ == "__main__":
    main(sys.argv[:])
