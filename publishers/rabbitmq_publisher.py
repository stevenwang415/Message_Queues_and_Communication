import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    channel.exchange_declare(exchange = 'logs', exchange_type = 'fanout')
    
    try:
        while True:
            message = input("Enter message to publish: ")
            if message.lower() == 'exit':
                print('Exiting...')
                break
            channel.basic_publish(exchange = 'logs', routing_key = '', body = message)
            print(f"Sending message: {message}")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        connection.close()

if __name__ == '__main__':
    main()