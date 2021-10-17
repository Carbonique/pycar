from servo_driver import servo

class Front_Wheels(object):

    def __init__(self):
        "Create front wheels object"
        self.Front_Wheels = Servo(0,500,2500,0,180)
        
   # def steer_To_Angle(self, angle):
   #     "Set front wheels to angle"
   #     self.front_wheels.angle = angle
        