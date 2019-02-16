from pi_server import serverViewer

server = serverViewer("cat", "dog")
server.initialize_server()
server.capture_stream()
