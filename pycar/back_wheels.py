from drivers.Motor import Motor

class back_wheels:
    
    def __init__(self):
        
        #PWM pins for speed
        self._pwmLeft = 4
        self._pwmRight = 5
        
        #BCM pins for driving direction
        self._bcmLeft = 17
        self._bcmRight = 27
        
        self._left_motor = Motor(self._bcmLeft, self._pwmLeft)
        self._right_motor = Motor(self._bcmRight,self._pwmRight)
        self.left_motor.speed = 0
        self.right_motor.speed = 0

    def forward(self):
        self._left_motor.forward()
        self._right_motor.forward()
        
    def reverse(self):    
        self._left_motor.reverse()
        self._right_motor.reverse()
    
    @property
    def speed(self):
        return (self._left_motor.speed +  self._right.motor.speed) / 2  
    
    @speed.setter
    def speed(self, speed):
        self._left_motor.speed = speed
        self._right_motor.speed = speed    
    
    @property    
    def stop(self):
        self._left_motor.stop()
        self._right_motor.stop() 