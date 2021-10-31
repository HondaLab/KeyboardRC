#! /usr/bin/python3
# Yasushiu Honda 2021 9/8
# Capture frames from PiCamera and record them to /tmp 

import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import modules.keyin as keyin

class PI_CAMERA():
   def __init__(self,width,height):
      
      # カメラの解像度 例：640x480, 320x240
      self.RES_X=int( width )
      self.RES_Y=int( height )
      
      # initialize the camera and grab a reference to the raw camera capture
      #カメラを初期化，カメラへのアクセス？ルート？オブジェクト作成？
      self.cam = PiCamera()
      self.cam.framerate = 30  #フレームレート
      self.cam.brightness = 50 #明るさ
      #cam.saturation = 50

      self.cam.awb_mode='auto'
      #list_awb = ['off', 'auto', 'sunlight', 'cloudy', 'shade']
      self.cam.iso=200
      self.cam.shutter_speed=1000000
      self.cam.exposure_mode = 'auto' # off, auto, fixedfps
      time.sleep(1)
      #self.g = self.cam.awb_gains
      #self.cam.awb_mode = 'off'
      #self.cam.awb_gains = self.g

      self.cam.resolution = (self.RES_X, self.RES_Y)
      self.cam.rotation=180
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
    OUT_FILE="/tmp/output.avi"
    print("# Captured movie is written in %s ." % OUT_FILE)
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    record_fps=9
    width=1200
    height=912
    print("# Resolution: %5d x %5d" % (width,height))
    size = (width, height)
    crop_left = 220
    crop_right = 1140
    crop_upper = 90
    crop_lower = 600
    crop_h=crop_lower - crop_upper 
    crop_w=crop_right - crop_left
    print("# Crop: %5d x %5d" % (crop_w,crop_h))
    vw = cv2.VideoWriter(OUT_FILE, fmt, record_fps, (crop_w,crop_h))
    #vw = cv2.VideoWriter(OUT_FILE, fmt, record_fps, (width,height))

    cam = PI_CAMERA(width,height)
    frame=cam.capture()
    #bbox=cv2.selectROI(frame,False)
    #print(bbox)

    key=keyin.Keyboard()
    ch='c'

    now=time.time()
    start=now
    print("# To stop, input 'q' in this terminal.")
    while ch!='q':
        now=time.time()
        print("\r time: %8.2f " % (now-start), end='')
        ch=key.read()
        try: 
            capt = cam.capture()
            #print(len(v) for v in capt)
            frame = capt[crop_upper:crop_lower,crop_left:crop_right,:]
            frame = cv2.resize(frame,(crop_w,crop_h))
            show_size=(800,608)
            show=cv2.resize(frame,show_size)
            cv2.imshow("Front View", show)
            cv2.waitKey(1)
            vw.write(frame)
        except KeyboardInterrupt:
            print("ctrl + C ")
            cv2.destroyAllWindows()
            vw.release()
        time.sleep(0.5)

    cv2.destroyAllWindows()
    vw.release()
    print("\n # Bye-bye \n")
