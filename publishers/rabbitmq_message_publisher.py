import pika
import time
import sys
import os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    try:
        while True:
            message = input("Please enter messages (Type 'exit' to leave): ")
            if message.lower() == 'exit': # add this feature if the user want to leave
                print('Exiting... have a nice day!')
                break
            
            channel.basic_publish(
                exchange='',
                routing_key='task_queue',
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                ))
            print(f" [x] Sent {message}")
            time.sleep(1)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

    connection.close()

if __name__ == '__main__':
    main()