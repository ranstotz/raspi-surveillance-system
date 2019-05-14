from pi_client import clientStreamer

client = clientStreamer()

client.connect_streaming_socket("18.214.123.134", "5050")
client.start_camera()
client.begin_stream()

