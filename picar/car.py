from Camera import Camera
from ServoDriver import Servo
from back_wheels import back_wheels
import time

class car:
    
    def __init__(self):
        self.front_wheels = Servo(0,500,2500,40,140, 0)
        self.back_wheels = back_wheels()
        self.Camera = Camera()
        



