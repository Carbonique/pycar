from drivers.servo import Servo

class Camera():
    
    def __init__(self):
        
        self._pan_pwm_channel = 1
        self._pan_servo_min_pulse = 500
        self._pan_servo_max_pulse = 2500
        self._pan_servo_min_angle = 1
        self._pan_servo_max_angle = 179
        self._pan_servo_offset = 0

        self._tilt_pwm_channel = 2
        self._tilt_servo_min_pulse = 1000
        self._tilt_servo_max_pulse = 2000
        self._tilt_servo_min_angle = 60
        self._tilt_servo_max_angle = 140
        self._tilt_servo_offset = 0

        self._panServo = Servo( "camera (pan)",
                                self._pan_pwm_channel, 
                                self._pan_servo_min_pulse, 
                                self._pan_servo_max_pulse,
                                self._pan_servo_min_angle,
                                self._pan_servo_max_angle,
                                self._pan_servo_offset
                                )
        self._panServo.neutral()
       
        self._tiltServo = Servo( "camera (tilt)",
                                self._tilt_pwm_channel, 
                                self._tilt_servo_min_pulse, 
                                self._tilt_servo_max_pulse,
                                self._tilt_servo_min_angle,
                                self._tilt_servo_max_angle,
                                self._tilt_servo_offset
                                )
        self._tiltServo.neutral()

    @property
    def pan(self):
        return self._panServo.angle

    @pan.setter
    def pan(self, angle):
        self._panServo.angle = angle
    
    def right(self, angle):
        self.pan = (self.pan - angle)

    def left(self, angle):
        self.pan = (self.pan + angle)

    @property
    def tilt(self):
        return self._tiltServo.angle

    @tilt.setter
    def tilt(self, angle):
        self._tiltServo.angle = angle

    def up(self, angle):
        self.tilt = (self.tilt - angle)

    def down(self, angle):
        self.tilt = (self.tilt + angle)

