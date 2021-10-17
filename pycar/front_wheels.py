from drivers.Servo import Servo

class front_wheels:

    def __init__(self):
        self.front_wheels = Servo(0,500,2500,40,140,0)
        self.front_wheels.neutral

    @property
    def steer(self):
        return self.steer
    
    @steer.setter
    def steer(self, angle):
        self.front_wheels.angle = angle
