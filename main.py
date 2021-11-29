"""
Style server service main
"""
import json
import sys
import pika


def callback(channel, method, _, body):
    """
    Callback function for receiving message
    """
    body = json.loads(body)
    print(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():
    """
    Main function
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('10.211.55.23'))
    channel = connection.channel()
    queue_name = "program_style"
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            print('Interrupted')
            sys.exit(0)
        except SystemExit:
            print('Interrupted')
            raise
