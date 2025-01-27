import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:5556')
    
    try: 
        while True:
            message = socket.recv_string()
            print(f'Received request: {message}')
            socket.send_string(f'{message}')
    except KeyboardInterrupt:
        print("Exiting...")
        
    socket.close()
    context.term()

if __name__ == '__main__':
    main()