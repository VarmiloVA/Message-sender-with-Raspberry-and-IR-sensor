#Librería que gestiona los pines de raspberry
from gpiozero import MotionSensor

class Sensor:
    """La clase que se encarga de gestionar el sensor"""
    def __init__(self):
        self.mailbox = False
        #Se establece el pin en el que el sensor está conectado
        self.pir = MotionSensor(23)

    def check_movement(self):
        #Comprueba si el sensor ha detectado movimiento
        self.pir.wait_for_motion()
        return True