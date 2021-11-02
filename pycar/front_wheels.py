from drivers.servo import Servo

class Front_Wheels():
    
    def __init__(self):
        #PWM and specs for steering servo
        self._pwm_channel_steer = 0
        self._servo_min_pulse_steer = 500
        self._servo_max_pulse_steer = 2500
        self._servo_min_angle_steer = 40
        self._servo_max_angle_steer = 140
        self._servo_offset_steer = 0

        self.servo = Servo(     "front wheels",
                                self._pwm_channel_steer, 
                                self._servo_min_pulse_steer, 
                                self._servo_max_pulse_steer,
                                self._servo_min_angle_steer,
                                self._servo_max_angle_steer,
                                self._servo_offset_steer
                                )

        self.servo.neutral()

    @property
    def angle(self):
        return self.servo.angle

    @angle.setter
    def angle(self, angle):
        self.servo.angle = angle

    def turn_right(self, angle):
        self.angle = (self.angle + angle)

    def turn_left(self, angle):
        self.angle = (self.angle - angle)