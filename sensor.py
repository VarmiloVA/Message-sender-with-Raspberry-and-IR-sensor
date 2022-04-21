class Sensor:
    def __init__(self):
        self.movement = True

    def check_movement(self):
        """Check de movement status"""
        return self.movement