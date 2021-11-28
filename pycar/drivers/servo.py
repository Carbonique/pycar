from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
import time

# Based on https://github.com/adafruit/Adafruit_CircuitPython_Motor/blob/main/adafruit_motor/servo.py

class Servo:

    def __init__(self, name, pca_channel, min_pulse, max_pulse, min_angle, max_angle):
        "Create a new servo object (name, channel, servoMinPulse, servoMaxPulse"

        self._name = str(name)

        i2c_bus = busio.I2C(SCL, SDA)
        self._pca = PCA9685(i2c_bus)
        self._pca.frequency = 60
        self._pca_channel = pca_channel

        # Calculate pulse ranges
        self._min_pulse = min_pulse
        self._max_pulse = max_pulse
        self._pulse_range = self._max_pulse - self._min_pulse

        self._min_duty = int((min_pulse * self._pca.frequency) / 1000000 * 0xFFFF)
        self._max_duty = (max_pulse * self._pca.frequency) / 1000000 * 0xFFFF
        self._duty_range = int(self._max_duty  - self._min_duty)

        # Calculate ranges in degrees
        self._min_angle = min_angle
        self._max_angle = max_angle
        self._actuation_range = 180

        self.angle = 90
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
            self._pca.channels[self._pca_channel].duty_cycle = int(self._convert_angle_to_duty_cycle(angle))

            self._angle = angle
            print(f"Setting {self._name} to angle {angle}")
        else:
            print(f"{self._name} angle {angle} is not in min max range: {self._min_angle} - {self._max_angle}")


##############################################################################

#Function for converting angle to duty cycle

##############################################################################

    def _convert_angle_to_duty_cycle(self, angle):
        "Convert angle given by user to duty cycle"
        fraction = angle / self._actuation_range
        return self._min_duty + int(fraction * self._duty_range)
##############################################################################

#Helper

##############################################################################

    def neutral(self):
        self.angle = 90
