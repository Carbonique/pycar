import Adafruit_PCA9685
import time

class Servo(object):
    "Create a new servo object (channel, servoMinPulse, servoMaxPulse, servoMinAngle, servoMaxAngle"
    
    def __init__(self, channel, servoMinPulse, servoMaxPulse, servoMinAngle, servoMaxAngle, offset):

        self._offset = offset
        self._angle = 0
        
        self._pwm = Adafruit_PCA9685.PCA9685()
        self._pwm_channel = channel
        self._pwm.set_pwm_freq(60)
        
        self._servoMinPulse = servoMinPulse
        self._servoMaxPulse = servoMaxPulse
        self._servoMinAngleOffsetted = servoMinAngle + self._offset
        self._servoMaxAngleOffsetted = servoMaxAngle + self._offset
        
        #1 second has 16666,7 microseconds (us). A 12-bit pwm has 16666,7/12 = 4096 increments per second
        incrementsPerSecond = 4.096
        
        self._servoMin = self._servoMinPulse / incrementsPerSecond
        self._servoMax = self._servoMaxPulse / incrementsPerSecond
        
        #Set Servo to neutrla
        #self.neutral()
        
##############################################################################

#Functions for calculating pulserange and pulsewidth

##############################################################################        
    
    def _calculate_Pulserange(self):
        "A function that returns the pulserange"
        pulseRange = self._servoMax - self._servoMin
        return pulseRange
    
    def _calculate_Pulse_Width_Per_Degree(self):
        "A function that returns the pulses needed to turn the servo 1 degree"
        #Servo has range from 0 to 180, which is 181 degrees
        servoMaxDegrees = 181
        
        #Pulserange divided by servoMaxDegrees results in the pulse needed to turn 1 degree
        return self._calculate_Pulserange() / servoMaxDegrees 

##############################################################################

#Functions for calculating angles

##############################################################################            
    def _angle_Within_Range(self, angle):
        "A function that checks whether the user specified angle is in range"
        return angle in range(self._servoMinAngleOffsetted, self._servoMaxAngleOffsetted)

    def _calculate_Pulse_Width_For_Angle(self, angle):
        "A function that returns the pulse width needed to turn the servo to a specified angle"
        #Return the pulse width needed for a specified angle 
        pulseWidthPerDegree = self._calculate_Pulse_Width_Per_Degree()
        
        return(self._servoMin + (angle * pulseWidthPerDegree))

        
##############################################################################

#Functions for setting angles

##############################################################################           
    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, angle):
        "A function that sets the servo to an angle specified by the user (arguments: angle)"
        offsettedAngle = angle + self._offset
        
        if self._servo_Not_Already_In_Angle(angle) is True:
            if self._angle_Within_Range(offsettedAngle):
                
                #Move servo to
                self._move_Servo_To(offsettedAngle)
                
                #set angle property to user inputted angle
                self._angle = angle
            else:
                print("Angle outside of range")
    
    def _servo_Not_Already_In_Angle(self, angle):
        "A function that checks whether the servo is already set in the inputted angle"
        if angle == self.angle:
            print("Servo already in specified angle")
            return False         
        else:
            return True
                 
    def neutral(self):
        self.angle = 90     
        
##############################################################################

#Helper functions

##############################################################################            
    def _move_Servo_To(self, angle):
        pwm_for_angle = int(self._calculate_Pulse_Width_For_Angle(angle))
        self._pwm.set_pwm(self._pwm_channel, 0, pwm_for_angle)
    
        





