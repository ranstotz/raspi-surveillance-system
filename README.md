# Raspberry Pi Surveillance System

The goal of this project was to stream live video from the Rasperry Pi (Camera Module) to the browser. This repo contains the code executed on the Rasperry Pi and streams the image frames to a server via message queue using Python.

## Overview

The system creates two socket connections with the server upon browser request. First, a streaming connection for sending encoded JPEG images and, second, a messaging connection to ensure both the Pi and the server are in-sync with both requests made and the overall state of the system. These two connections are on separate threads to avoid streaming disruption.

Both connections communicate via TCP using ZMQ which is a lightweight and fast messaging package.

See docstrings for more information.
