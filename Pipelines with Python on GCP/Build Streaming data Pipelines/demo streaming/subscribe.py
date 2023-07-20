# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 23:10:06 2023

@author: Andres
"""

from google.cloud import pubsub_v1
import time
import os

if __name__ == "__main__":
    
    # Replace 'my-service-account-path' with your service account path
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'my-service-account-path'
    
    # Replace 'my-subscription' with your subscription id
    subscription_path = args.subscription_path
    
    subscriber = pubsub_v1.SubscriberClient()
 
    def callback(message):
        print(('Received message: {}'.format(message)))    
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    while True:
        time.sleep(60)