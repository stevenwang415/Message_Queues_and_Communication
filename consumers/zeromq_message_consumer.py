import zmq
import sys
import pika

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://localhost:5557")

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        socket.send(body)
        ch.basic_ack(delivert_tag = method.delivery_tag)
    
    channel.basic_qos(prefetch_count = 1)
    channel.basic_consume(queue = 'task_queue', on_message_callback = callback, auto_ack = False)
    
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    finally:
        connection.close()
        socket.close()
        context.term()
        
if __name__ == '__main__':
    main()
