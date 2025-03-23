import paho.mqtt.client as mqtt
from prueba import settings
import json

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
       print('Connected successfully')
       mqtt_client.subscribe('sensor/distancia')
   else:
       print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):

    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')

def connect_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
    client.connect(settings.MQTT_BROKER_URL, settings.MQTT_BROKER_PORT, 60)
    client.subscribe(settings.MQTT_TOPIC)
    client.loop_start()
    print("Conectado a EMQX y suscrito a:", settings.MQTT_TOPIC)

    


