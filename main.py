"""
Style server service main
"""
import json
import os
import sys

import pika
import requests

from service import java, python


def callback(channel, method, _, body):
    """
    Callback function for receiving message
    """
    body = json.loads(body)
    path = os.getenv("SUBMISSION_URL")+"/"+str(body["submission_id"])+"/style"
    if body["language"] == "java":
        result = java.check(str(body["submission_id"]), body["source_code"])
        res = requests.patch(path, json=result)
        if os.getenv("LOG") == "1":
            print(res.text)
            print (res.request.body)
    elif body["language"] == "python3":
        result = python.check(str(body["submission_id"]), body["source_code"])
        res = requests.patch(path, json=result)
        if os.getenv("LOG") == "1":
            print(res.text)
            print (res.request.body)
    else:
        result = None
        if os.getenv("LOG") == "1":
            msg = "submission_id: %s language %s not supported"
            print(msg % (body["submission_id"], body["language"]))
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():
    """
    Main function
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=os.getenv("RABITMQ")))
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
