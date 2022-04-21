#Libraries
from time import sleep
import datetime
import pyttsx3

#My own files
import sensor

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

    def run(self):
        self.sensor_message()
    
    def sensor_message(self):
        self.movement = self.sensor.check_movement()
        self._voice_message(self.movement)

    def _voice_message(self, movement):
        if movement == True:
            print('Ha llegado una carta')
            engine.say('Ha llegado una carta')
            engine.runAndWait()
            engine.stop()
        
        elif movement == False:
            print('El buzón está vacío, volviendo a comprobar en 10 minutos')
            engine.say('El buzón está vacío, volviendo a comprobar en 10 minutos')
            engine.runAndWait()
            engine.stop()

while __name__ == '__main__':
    """The program will work only if it's ejecuted as main"""
    #if hora esta entre las horas de trabajo:
    rb = Raspberry()
    rb.run()
    sleep(10)