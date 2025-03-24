import time
import paho.mqtt.client as mqtt
from prueba import settings
import json

import logging

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
       print(f"Connected with result code {rc}")
       mqtt_client.subscribe('sensor/distancia', qos=0)
    else:
        print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):

    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')

    

def connect_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
    print(f"Connecting to MQTT broker at {settings.MQTT_BROKER_URL}:{settings.MQTT_BROKER_PORT}")

    connected = 0
    while not connected:
        try:
                client.connect(host=settings.MQTT_BROKER_URL, port=settings.MQTT_BROKER_PORT, keepalive=60)
                client.loop_start()
                connected = 1
        except:
                time.sleep(5)


    


