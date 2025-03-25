from django.apps import AppConfig
import os
import time
from threading import Thread

class SensoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sensores'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'true':  # Evita ejecutar dos veces con runserver
            return

        from .mqtt import connect_mqtt

        while True:
            client = connect_mqtt()
            if client:
                break  # Sale del bucle si la conexión fue exitosa
            print("Reintentando conexión MQTT en 5 segundos...")
            time.sleep(5)