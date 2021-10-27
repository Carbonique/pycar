import os
import cv2
import datetime
from datetime import datetime
from base_camera import BaseCamera
import numpy as np
import math
import sys
from matplotlib import pyplot as plt
import glob
import pickle



class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        camera.set(3,320) #Setting webcam's image width 
        camera.set(4,240) #Setting webcam' image height

        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame

            _, frame = camera.read()
            
            test = LineDetection.process_Image(frame)
          
            yield cv2.imencode('.jpg', test)[1].tobytes()
            
   