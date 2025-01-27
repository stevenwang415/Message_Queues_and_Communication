import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://localhost:5555')
    socket.setsockopt_string(zmq.SUBSCRIBE, '')
    
    try:
        while True:
            message = socket.recv_string()
            print(f'Receiving message: {message}')
    
    except KeyboardInterrupt:
        print('Stopping...')
    
    finally:
        socket.close()
        context.term()
    
if __name__ == '__main__':
    main()
        
            