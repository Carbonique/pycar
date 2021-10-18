from drivers.servo import Servo
from drivers.motor import Motor

class car:
    
    def __init__(self):
        #PWM pins for motor speed
        self._pwm_channel_left_motor = 4
        self._pwm_channel_right_motor = 5
        
        #BCM pins for motor driving direction
        self._bcm_left_motor = 17
        self._bcm_right_motor = 27

        #PWM and specs for steering servo
        self._pwm_channel_steer = 0
        self._servo_min_pulse_steer = 500
        self._servo_max_pulse_steer = 2500
        self._servo_min_angle_steer = 40
        self._servo_max_angle_steer = 140
        self._servo_offset_steer = 0

        self.front_wheels = Servo(
                                self._pwm_channel_steer, 
                                self._servo_min_pulse_steer, 
                                self._servo_max_pulse_steer,
                                self._servo_min_angle_steer,
                                self._servo_max_angle_steer,
                                self._servo_offset_steer
                                )

        self.left_motor = Motor(self._bcm_left_motor, self._pwm_channel_left_motor)
        self.right_motor = Motor(self._bcm_right_motor,self._pwm_channel_right_motor)
        self.left_motor.speed
        self.right_motor.speed = 0

        self.front_wheels.neutral

    def steer(self, angle):
        self.front_wheels.angle = angle

    def drive(self, speed):
        self.left_motor.speed = speed
        self.right_motor.speed = speed


audi = car()
audi.steer(139)
