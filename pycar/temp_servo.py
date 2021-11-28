from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
import time

# Credits to https://docs.onion.io/omega2-maker-kit/maker-kit-servo-controlling-servo.html
# for explaining most of the logic in this class

class Servo:

    def __init__(self, name, pca_channel, min_pulse, max_pulse, min_angle, max_angle):
        "Create a new servo object (name, channel, servoMinPulse, servoMaxPulse"

        self._name = str(name)
        self._offset = offset
        self._angle = 90

        i2c_bus = busio.I2C(SCL, SDA)
        self._pca = PCA9685(i2c_bus)
        self._pca.frequency = 60
        self._pca_channel = pca_channel

        # Calculate pulse ranges
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self._pulse_range = self._max_pulse - self._min_pulse

        # Calculate ranges in degrees
        self._min_angle = min_angle
        self._max_angle = max_angle

        # Calculate the step (us / degree)
        self.step = self._pulse_range / 135 #135 is the actuation range for the servo. 135 is arbitrary. Modern servos can reach 180 degrees range

        # Calculate the period (in us)
        self.period = (1000000 / self._pca.frequency)


##############################################################################

#Functions for setting angles

##############################################################################
    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        "A function that sets the servo to an angle specified by the user (arguments: angle)"
        if self._min_angle <= angle <= self._max_angle: #interval comparison (same as if-statement in range, but faster)

            #Move to angle
            self._pca.channels[self._pca_channel].duty_cycle = self._convert_angle_to_duty_cycle(angle)

            self._angle = angle

        else:
            print(f"Angle {angle} is not in min max range: {self._min_angle} - {self._max_angle}")

    def _convert_angle_to_duty_cycle(self, angle):
        "Convert angle given by user to duty cycle"

        pulse_width = angle * self.step + self.min_pulse

        duty = (pulseWidth * 100) / float(self.period)

        return duty
