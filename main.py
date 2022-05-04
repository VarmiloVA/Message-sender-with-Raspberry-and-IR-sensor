#Libraries
from time import sleep
import datetime
import pyttsx3
import json

#My own files
import sensor
from sms import *

class main:
    def __init__(self, flag):
        self.sensor = sensor.Sensor()
        self.start_time = datetime.time(8, 0, 0)
        self.finish_time = datetime.time(20, 0, 0)

        self.out_of_service = False

        self.flag = flag

        with open("data.json", "r") as f:
            c = f.read()
            data = json.loads(c)

        self.users = data['users']

    def run(self):
        #self.time_now = datetime.datetime.now()
        # if self.time_now.hour < self.start_time.hour or self.time_now.hour > self.finish_time.hour:
        #     engine.say('Es antes de las 8 de la mañana, no creo que ningún repartidor trabaje tan pronto')
        #     engine.runAndWait()
        #     engine.stop()

        #     self.out_of_service = True
        
        # elif self.time_now.hour > self.finish_time.hour:
        #     engine.say('Es más tarde de las 8 de la tarde, no creo que ningún repartidor trabaje tan tarde')
        #     engine.runAndWait()
        #     engine.stop()

        #     self.out_of_service = True

        # else:
        self.sensor_message()

    def sensor_message(self):
            user = self.users['buzon1']
            self._notify(user)

    def _notify(self, user):
            message = f'Ha llegado correo al buzón de {user["owner"]}'
            print(message)

            if self.flag != 1:
                sms_send('Ha llegado correo al buzón', user['phone_number'])

k = sensor.Sensor()
movement = k.check_movement()
while movement:
    flag = 0
    while __name__ == '__main__':
        """El programa solo va a funcionar si es ejecutado como principal"""
        rb = main(flag)

        if flag != 2:
            rb.run()
            flag += 1
            sleep(1.5)
        elif flag == 2:
        
            if rb.sensor.check_movement() != False:
                break
    break