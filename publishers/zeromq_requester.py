import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:5556')

    for request in range(10):
        print(f'Sending request: {request}')
        socket.send_string(f'{request}')
        message = socket.recv_string()
        print(f'Received reply: {request} [ {message} ]')

    socket.close()
    context.term()

if __name__ == '__main__':
    main()
