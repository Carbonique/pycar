import RPi.GPIO as GPIO
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
import time

class Motor:

    def __init__(self, direction_channel, pca_channel):
        "Create a motor object (arguments: direction_channel, pca_channel"

        # Best is to keep the min and max of equal size for now (e.g. 10 and -10, 20 and -20)
        # Some formulas depend on this.
        self._min_speed = -100
        self._max_speed = 100
        self._speed = 0

        #Setting GPIO pins
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self._direction_channel = direction_channel
        GPIO.setup(self._direction_channel, GPIO.OUT)
        self.direction = None

        i2c_bus = busio.I2C(SCL, SDA)
        self._pca = PCA9685(i2c_bus)
        self._pca.frequency = 60
        self._pca_channel = pca_channel

        # Duty_cycle is 16 bits to match other PWM objects
        # But the PCA9685 will only actually give 12 bits of resolution.
        self._pca_min_duty_cycle = 0
        self._pca_max_duty_cycle = 0xFFFF

##############################################################################

#Functions for setting motor directions

##############################################################################

    def set_forward(self):
        "Set motor direction to forward"
        GPIO.output(self._direction_channel,0)
        self.direction_is_forward = True

    def set_reverse(self):
        "Set motor direction to reverse"
        GPIO.output(self._direction_channel,1)
        self.direction_is_forward = False

##############################################################################

#Functions for setting speeds

##############################################################################

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        "Set speed to speed given by user (argument: speed)"
        if speed <= 0:
            self.set_reverse()
        else:
            self.set_forward()

        if self._min_speed <= speed <= self._max_speed: #interval comparison (same as if-statement in range, but faster)

            #Motor speed
            self._pca.channels[self._pca_channel].duty_cycle = self._convert_speed_to_duty_cycle(speed)

            #Set speed property
            self._speed = speed

        else:
            print(f"Speed {speed} is not in min max range: {self._min_speed} - {self._max_speed}")

##############################################################################

#Function for converting speed to duty cycle

##############################################################################

    def _convert_speed_to_duty_cycle(self, speed):
        "Convert speed given by user to duty cycle"
        if speed == 0:
            relative_speed = 0
        elif speed > 0:
            relative_speed = speed / self._max_speed
        else:
            relative_speed  = speed / self._min_speed

        return int(self._pca_max_duty_cycle * relative_speed)
