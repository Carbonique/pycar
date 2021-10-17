from drivers.Servo import Servo

class front_wheels:

    def __init__(self):
        self.front_wheels = Servo(0,500,2500,40,140,0)
        print ('hi')
        self.steer()

    def steer(self):
        self.front_wheels.angle = 80
        print ('steer')

test = front_wheels()