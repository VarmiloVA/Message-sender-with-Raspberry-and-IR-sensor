from gpiozero import MotionSensor

class Sensor:
    def __init__(self):
        self.mailbox = False
        self.pir = MotionSensor(23)

    def check_movement(self):
        """Check de movement status"""
        self.pir.wait_for_motion()
        return True