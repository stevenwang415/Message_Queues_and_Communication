import pika
import zmq
import time

def bridge_messages():
    # Setup RabbitMQ Connection
    rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = rabbit_connection.channel()
    channel.queue_declare(queue='hello')
    
    channel.queue_bind(queue='hello', exchange='logs', routing_key='')

    # Setup ZeroMQ Connection
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://*:5558")

    # Consume messages from RabbitMQ and forward to ZeroMQ
    for method_frame, properties, body in channel.consume('hello'):
        print("Received message from RabbitMQ:", body)
        socket.send_string(body.decode())
        print("Message forwarded to ZeroMQ")
        channel.basic_ack(method_frame.delivery_tag)

        time.sleep(1)  # Simulate work or control flow
    
    # Cleanup
    rabbit_connection.close()
    socket.close()
    context.term()
    

if __name__ == "__main__":
    bridge_messages()
