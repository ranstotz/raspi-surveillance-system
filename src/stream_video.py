import sys
import os
import time
import threading
import zmq
import numpy as np
import yaml

from pi_client import Streamer

connection_flag = False

# configuration data
config_data = get_config('../config.yaml')


def message_handler():

    global connection_flag
    global exit_signal
    global config_data

    connected = "connected"
    disconnected = "disconnected"

    messaging_socket = zmq.Context().socket(zmq.SUB)
    messaging_socket.bind('tcp://*:' + str(config_data['listening_port']))
    messaging_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

    while not exit_signal.is_set():
        try:
            incoming_message = messaging_socket.recv_string()
            if incoming_message == connected:
                connection_flag = True
            elif incoming_message == disconnected:
                connection_flag = False
        except:
            pass
    return


def get_config(file_path):
    """ Returns configuration data in yaml file as a dict. """

    with open(file_path, 'r') as fp:
        return yaml.load(fp)


def main(argv):

    global connection_flag
    global exit_signal
    global config_data

    client = Streamer()
    client.connect_streaming_socket(
        str(config_data['connection_ip']), str(config_data['connection_port']))
    client.start_camera()

    # start stream
    for frame in client.camera.capture_continuous(client.rawCapture, format="bgr",
                                                  use_video_port=True):

        try:
            if exit_signal.is_set():
                break
            if connection_flag == True:
                client.encode_and_send_image(frame)
            client.rawCapture.truncate(0)

        except:
            break

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
            # let the process breath awaiting connection
            time.sleep(0.1)

    except KeyboardInterrupt:
        exit_signal.set()

    print "exit script"
