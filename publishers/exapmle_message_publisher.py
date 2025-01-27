import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    time.sleep(1)
    socket.send_string("Hello")
    print("Message sent!")