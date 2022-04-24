#Libraries
from collections import UserString
from time import sleep
import datetime
import pyttsx3
import json

#My own files
import sensor
from sms import *

#Setting up the voice.
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', 0.5)
speed = engine.getProperty('rate')
#Optimal speed is -50
engine.setProperty('rate', speed-50)

class Raspberry:
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
        self.time_now = datetime.datetime.now()
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
        movement = self.sensor.check_movement()

        if movement == 1:
            user = self.users['buzon1']
            if user['activated'] == 0:
                engine.say('Para comprobar tu correo primero has de dar de alta tu número de teléfono')
                engine.runAndWait()
                engine.stop()
            else:
                self._notify(user)
        
        elif movement == 2:
            user = self.users['buzon2']
            if user['activated'] == 0:
                engine.say('Para comprobar tu correo primero has de dar de alta tu número de teléfono')
                engine.runAndWait()
                engine.stop()
            else:
                self._notify(user)
        
        elif movement == 3:
            user = self.users['buzon3']
            if user['activated'] == 0:
                engine.say('Para comprobar tu correo primero has de dar de alta tu número de teléfono')
                engine.runAndWait()
                engine.stop()
            else:
                self._notify(user)
        
        elif movement == 4:
            user = self.users['buzon4']
            if user['activated'] == 0:
                engine.say('Para comprobar tu correo primero has de dar de alta tu número de teléfono')
                engine.runAndWait()
                engine.stop()
            else:
                self._notify(user)


    def _notify(self, user):
            message = f'Ha llegado correo al buzón de {user["owner"]}'
            print(message)
            engine.say(message)
            engine.runAndWait()
            engine.stop()

            if self.flag != 1:
                sms_send('Ha llegado correo al buzón', user['phone_number'])

flag = 0
while __name__ == '__main__':
    """The program will work only if it's ejecuted as main"""
    rb = Raspberry(flag)

    if flag != 2:
        rb.run()
        flag += 1
        sleep(1.7)
    elif flag == 2:
        engine.say('Fin del mensaje')
        engine.runAndWait()
        engine.stop()
        
        if rb.sensor.check_movement() != False:
            break
        else:
            sleep(15)