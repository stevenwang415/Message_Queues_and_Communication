import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
    
try:
    while True:
        message = socket.recv_string()
        print(f"Received request: {message}")
        
        message_send = input("Enter message to send (Ctrl + C to exit): ")
        socket.send_string(message_send)
finally:
    socket.close()
    context.term()