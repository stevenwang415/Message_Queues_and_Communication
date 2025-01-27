import zmq
import time

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind('tcp://*:5557')

    for num in range(100):
        task = f'Task: {num}'
        print(f'Sending {task}')
        socket.send_string(task)
        time.sleep(1)

    socket.close()
    context.term()

if __name__ == '__main__':
    main()
