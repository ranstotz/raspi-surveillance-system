from pi_client import clientStreamer

client = clientStreamer("doesn't", "matter")

client.start_camera()
client.begin_stream()

