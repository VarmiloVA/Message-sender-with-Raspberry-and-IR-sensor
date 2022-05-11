#Librerías
from time import sleep
import datetime
import pyttsx3
import json

#Archivos propios
import sensor
from sms import *

class main:
    """Esta es la clase principal que hereda y gestiona todo el programa"""
    def __init__(self):
        #Se establecen las variables y el horario de trabajo del sensor
        self.sensor = sensor.Sensor()
        self.start_time = datetime.time(8, 0, 0)
        self.finish_time = datetime.time(20, 0, 0)

        self.out_of_service = False

        #Se abre el archivo json, el cuál almacena la info de los usuarios
        with open("data.json", "r") as f:
            c = f.read()
            data = json.loads(c)

        self.users = data['users']

    def run(self):
        #Si el sensor está en el horario de trabajo se ejecuta el código
        self.time_now = datetime.datetime.now()
        if self.time_now.hour < self.start_time.hour or self.time_now.hour > self.finish_time.hour:
            self.out_of_service = True
        
        elif self.time_now.hour > self.finish_time.hour:
            self.out_of_service = True

        else:
            self.sensor_message()

    def sensor_message(self):
        #Se envía el mensaje al usuario
            user = self.users['buzon1']
            self._notify(user)

    def _notify(self, user):
        #Módulo de recurso para el envío de mensajes
            message = f'Ha llegado correo al buzón de {user["owner"]}'
            print(message)
            sms_send('Ha llegado correo al buzón', user['phone_number'])

#Se llama a la cláse sensor
sensor = sensor.Sensor()
movement = sensor.check_movement()


#Se ejecuta el programa
while __name__ == '__main__':
    """El programa solo va a funcionar si es ejecutado como principal"""
    if movement:
        main = main()
        main.run()
        break

    sleep(0.1)