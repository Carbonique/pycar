import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time

class Motor:
    
    def __init__(self, direction_channel, pwm_channel):
        "Create a motor object (arguments: direction_channel, pwm_channel"

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
        
        self._pwm = Adafruit_PCA9685.PCA9685()
        self._pwm.set_pwm_freq(60)
        self._pwm_channel = pwm_channel
        
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

#Functions for converting speed to pulsewidth

##############################################################################               

    def _convert_Speed_To_Pulsewidth(self, speed):
        "Convert speed given by user to a speed in pulse width"
        #1 second has 16666,7 microseconds (us). A 12-bit pwm has 16666,7/12 = 4096 increments per second. 
        motor_max_pulse = 4096 
        motor_min_pulse = 0

        pulse = int((speed - 0) * (motor_max_pulse - motor_min_pulse) / (self._max_speed - 0) + motor_min_pulse)

        # When the car is in reverse the pulse calculation will result in a negative value.
        # That negative value has to be inverted.
        if self.direction_is_forward is False:
            pulse = pulse * -1
  
        return pulse

    def _is_Speed_In_Min_Max_Range(self, speed):
        return speed in range(-100, 100)

##############################################################################

#Functions for setting speeds

##############################################################################       
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        "Set speed to speed given by user, first checks whether speed is in min max range (argument: speed)"
        if speed <= 0:
            self.set_reverse()
        else:
            self.set_forward()

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