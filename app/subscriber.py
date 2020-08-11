from google.cloud import pubsub_v1
from random import randint
import threading

received_messages = []

def callback(message):
    # if (randint(1, 10) < 5):
    #     return
    received_messages.append(message.data.decode('utf-8'))
    message.ack()

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path("sethmaxwl-playground", "chat-subscriber")
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

def listen_for_messages():
    with subscriber:
        try:
            streaming_pull_future.result()
        except:
            streaming_pull_future.cancel()

try:
    threading.Thread(target=listen_for_messages)
except:
    print("Error: unable to start thread.")

def get_messages():
    return received_messages