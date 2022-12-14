
from drivers.motor import Motor

class Back_Wheels:
    def __init__(self):

        #BCM pins for motor driving direction
        self._bcm_left_motor = 17
        self._bcm_right_motor = 27

        #PWM pins for motor speed
        self._pwm_channel_left_motor = 4
        self._pwm_channel_right_motor = 5

        self.left_motor = Motor(self._bcm_left_motor, self._pwm_channel_left_motor)
        self.right_motor = Motor(self._bcm_right_motor,self._pwm_channel_right_motor)


    @property
    def speed(self):
        return int((self.right_motor.speed + self.left_motor.speed) / 2)

    @speed.setter
    def speed(self, speed):
        self.right_motor.speed = speed
        self.left_motor.speed = speed

    def change_speed_by(self, speed):
        self.speed = (self.speed + speed)

    def stop(self):
        self.speed = 0
