import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect('tcp://localhost:5558')
    
    try:
        while True:
            task = socket.recv_string()
            if task.lower() == 'exit':
                print('Exiting...')
                break
            print(f'Processing {task}')
    except KeyboardInterrupt:
        print('Exiting...')
         
    socket.close()
    context.term()

if __name__ == '__main__':
    main()
