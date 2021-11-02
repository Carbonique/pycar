from drivers.servo import Servo
from back_wheels import Back_Wheels
from front_wheels import Front_Wheels
from camera import Camera

class Car:

    def __init__(self):
        self.front_wheels = Front_Wheels()
        self.back_wheels = Back_Wheels()
        self.camera = Camera()