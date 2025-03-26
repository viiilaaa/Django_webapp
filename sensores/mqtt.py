import paho.mqtt.client as mqtt
from prueba import settings
from .models import MedicionSensor, Sensor
from django.utils.dateparse import parse_datetime
import json
from django.utils import timezone


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
       print(f"Connected with result code {rc}")
       mqtt_client.subscribe('sensor/distancia', qos=0)
    else:
        print('Bad connection. Code:', rc)

def on_message(client, userdata, msg):
    # El mensaje llega en formato JSON
    data = json.loads(msg.payload.decode())

    # Procesar el mensaje, por ejemplo, obtener los datos
    sensor_id = data['sensor_id']
    distancia = data['distancia']
    fecha_medicion = data['fecha_medicion']  # La fecha también se recibe como parámetro

    # Convertir la fecha recibida a un formato DateTime
    fecha_medicion = parse_datetime(fecha_medicion)

    if fecha_medicion:
        fecha_medicion = timezone.make_aware(fecha_medicion, timezone.get_current_timezone())


    # Obtener el sensor relacionado
    try:
        sensor = Sensor.objects.get(id=sensor_id)
    except Sensor.DoesNotExist:
        # Si el sensor no existe, no hacemos nada o logueamos un error
        return

    # Guardar la medición
    medicion = MedicionSensor(sensor=sensor, distancia=distancia, fecha_medicion=fecha_medicion)
    medicion.save()

#MAX_RETRIES = 5  # Máximo de intentos de conexión
#RETRY_DELAY = 5 
#mqtt_client = None 
#def connect_mqtt():
#    global mqtt_client
#    if mqtt_client is not None:
#        print("MQTT client already running, skipping new connection.")
#        return mqtt_client

#    client = mqtt.Client()
#    client.on_connect = on_connect
#    client.on_message = on_message
#    client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
    
#    print(f"Connecting to MQTT broker at {settings.MQTT_BROKER_URL}:{settings.MQTT_BROKER_PORT}")

#    for attempt in range(MAX_RETRIES):
#        try:
#            client.connect(host=settings.MQTT_BROKER_URL, port=settings.MQTT_BROKER_PORT, keepalive=60)
#            thread = threading.Thread(target=client.loop_forever, daemon=True)  
#            thread.start()
#            print("MQTT connection established.")
#            mqtt_client = client  # Guardamos la instancia
#            return client
#        except Exception as e:
#            print(f"Connection attempt {attempt+1} failed: {e}")
#            time.sleep(RETRY_DELAY)

#    print("Failed to connect to MQTT broker after multiple attempts.")
#    return None

def connect_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

    try:
        print(f"Connecting to MQTT broker at {settings.MQTT_BROKER_URL}:{settings.MQTT_BROKER_PORT}")
        client.connect(settings.MQTT_BROKER_URL, settings.MQTT_BROKER_PORT, 60)
        client.loop_start()
        return client
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None
