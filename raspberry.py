#Libraries
from time import sleep
import datetime
import pyttsx3

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
    def __init__(self):
        self.sensor = sensor.Sensor()
        self.start_time = datetime.time(8, 0, 0)
        self.finish_time = datetime.time(20, 0, 0)

        self.out_of_service = False

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
        self.movement = self.sensor.check_movement()
        self._voice_message(self.movement)

    def _voice_message(self, movement):
        if movement == True:
            print('Ha llegado correo al buzón')
            engine.say('Ha llegado correo al buzón')
            engine.runAndWait()
            engine.stop()

            sms_send('Ha llegado correo al buzón')
        
        elif movement == False:
            print('El buzón está vacío, volviendo a comprobar en 10 minutos')
            engine.say('El buzón está vacío, volviendo a comprobar en 10 minutos')
            engine.runAndWait()
            engine.stop()

            sms_send('El buzón está vacío')

flag = 0
while __name__ == '__main__':
    """The program will work only if it's ejecuted as main"""
    rb = Raspberry()

    if flag != 3:
        rb.run()
        flag += 1
        sleep(1.7)
    elif flag == 3:
        engine.say('Fin del mensaje')
        engine.runAndWait()
        engine.stop()
        
        if rb.sensor.movement == True:
            break
        else:
            sleep(600)