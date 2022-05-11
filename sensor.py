import RPi.GPIO as GPIO  #A no ser que se esté en un sistema raspbian, esta librería aparecerá como error.
class Sensor:
    """La clase que se encarga de gestionar el sensor"""
    def __init__(): 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.IN)

    def check_movement():
        sensor = GPIO.input(23)     #Lee el estado del sensor.

        if sensor == 0:     #Si el sensor detecta movimiento.
            return True
        elif sensor == 1:   #Si el sensor no detecta movimiento.
            return False