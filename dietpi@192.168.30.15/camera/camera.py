from ServoDriver import Servo
import Stream
import cv2


class Camera(object):
    
        #def __init__(self):
            #Instatiate two servo objects
            #self.tiltServo = Servo(2, 1000,2000, 60, 120, 0)
            #self.panServo = Servo(1,500, 2400, 45, 135, 20)

        def stream_Image(self):
            Stream.main()
            
            


camera = Camera()
camera.stream_Image()

