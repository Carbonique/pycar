import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time

class Motor:
    
    def __init__(self, direction_channel, pwm_channel):
        "Create a motor object (arguments: direction_channel, pwm_channel"
        self._min_speed = 0
        self._max_speed = 100
        self._speed = 0
        
        #Setting GPIO pins
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        self._direction_channel = direction_channel
        GPIO.setup(self._direction_channel, GPIO.OUT)
        
        self._pwm = Adafruit_PCA9685.PCA9685()
        self._pwm.set_pwm_freq(60)
        self._pwm_channel = pwm_channel
        
##############################################################################

#Functions for setting motor directions

##############################################################################           
    
    def forward(self):
        "Set motor direction to forward"
        GPIO.output(self._direction_channel,0)
        
    def reverse(self):
        "Set motor direction to reverse"
        GPIO.output(self._direction_channel,1)
        
##############################################################################

#Functions for converting speed to pulsewidth

##############################################################################               

    def _convert_Speed_To_Pulsewidth(self,speed):
        "Convert speed given by user to a speed in pulse width"
        #1 second has 16666,7 microseconds (us). A 12-bit pwm has 16666,7/12 = 4096 increments per second. 
        motor_max_pulse = 4096
        motor_min_pulse = 0

        return int((speed - self._min_speed) * (motor_max_pulse - motor_min_pulse) / (self._max_speed - self._min_speed) + motor_min_pulse)
    
    def _is_Speed_In_Min_Max_Range(self, speed):
        return speed in range(self._min_speed, self._max_speed)

##############################################################################

#Functions for setting speeds

##############################################################################       
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        "Set speed to speed given by user, first checks whether speed is in min max range (argument: speed)"
        if self._is_Speed_In_Min_Max_Range(speed) is True:
        
            #Motor speed
            self._set_Speed_To(speed)
            
            #Set speed property
            self._speed = speed
        else: 
            print("Speed {} is not in min max range: {} - {}".format(speed, self._min_speed, self._max_speed))
        
    def stop(self):
        "Stop car (= set speed to 0)"
        self.speed = 0


##############################################################################

#Helper functions

##############################################################################            
    def _set_Speed_To(self, speed):
        speedInPwm = self._convert_Speed_To_Pulsewidth(speed)
        self._pwm.set_pwm(self._pwm_channel, 0, speedInPwm)     