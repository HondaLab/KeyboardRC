#! /usr/bin/python3
# Yasushiu Honda 2021 9/8
# Capture frames from PiCamera and record them to /tmp 

import datetime
import numpy as np
import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from subprocess import Popen
#sokcet tuusinn kannkei
import socket
#import socket1a as sk
import modules.keyin as keyin

class PI_CAMERA():
   def __init__(self):
      
      # カメラの解像度 例：640x480, 320x240
      self.RES_X=int( 320 )
      self.RES_Y=int( 320 )
      
      # initialize the camera and grab a reference to the raw camera capture
      #カメラを初期化，カメラへのアクセス？ルート？オブジェクト作成？
      self.cam = PiCamera()
      self.cam.framerate = 30  #フレームレート
      self.cam.brightness = 60 #明るさ
      #cam.saturation = 50

      self.cam.awb_mode='auto'
      #list_awb = ['off', 'auto', 'sunlight', 'cloudy', 'shade']
      self.cam.iso=800
      self.cam.shutter_speed=1000000
      self.cam.exposure_mode = 'auto' # off, auto, fixedfps
      time.sleep(3)
      self.g = self.cam.awb_gains
      self.cam.awb_mode = 'off'
      self.cam.awb_gains = self.g

      self.cam.resolution = (self.RES_X, self.RES_Y)
      self.cam.rotation=0
      self.cam.meter_mode = 'average' # average, spot, backlit, matrix
      self.cam.exposure_compensation = 0
      self.rawCapture = PiRGBArray(self.cam, size=(self.RES_X, self.RES_Y))

      self.rawCapture.truncate(0) # clear the stream for next frame

   def capture(self):
      tmp = self.cam.capture_continuous(self.rawCapture, format="bgr", use_video_port="True")
      cap = next(tmp)
      frame = cap.array

      self.rawCapture.truncate(0) # clear the stream for next frame

      return frame


if __name__ == "__main__":
    # For recording
    OUT_FILE="/tmp/output.mp4"
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    record_fps=9
    width=320
    height=320
    size = (width, height)
    vw = cv2.VideoWriter(OUT_FILE, fmt, record_fps, size)

    select_hsv="n"     
    cam = PI_CAMERA()

    key=keyin.Keyboard()
    ch='c'

    now=time.time()
    start=now
    while ch!='q':
        now=time.time()
        ch=key.read()
        try: 
            frame = cam.capture()
            cv2.imshow("Front View", frame)
            cv2.waitKey(1)

            vw.write(frame)

        except KeyboardInterrupt:
            print("ctrl + C ")
            cv2.destroyAllWindows()
            vw.release()

    cv2.destroyAllWindows()
    vw.release()
