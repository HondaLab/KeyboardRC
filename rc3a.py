#!/usr/bin/python3

# ssr2_rc2a.py
# CC BY-SA Yasushi Honda 2020 2/25 

# How to execute
# sudo pigpiod
# pyhton3 hjkl1.py 

import keyin # キーボード入力を監視するモジュール
import motor5a as mt # pwmでモーターを回転させるためのモジュール
import motor1 as sv # カメラサーボ
import time
import pigpio

def Run(mL,mR,left,right):
   if left<-100: left = -100
   if left>100: left = 100
   mL.run(left)
   if right<-100: right = -100
   if right>100: right = 100
   mR.run(right)


if __name__=="__main__":
   STEP=8
   SLEEP=0.1
   HANDLE_STEP=5
   HANDLE_TIME=0.3
   TRIM_STEP=3
   TRIM_TIME=0.2

   mL=mt.Lmotor(17)
   mR=mt.Rmotor(18)
   csv=sv.Rmotor(27)
   
   key = keyin.Keyboard()
   ch="c"
   print("Input q to stop.")
   left=0
   right=0
   while ch!="q":
    
      ch = key.read()

      print("\r %4d %4d" % (left,right),end='')

      try:

         if ch == "j" :
            #TRIM_STEP=int(0.5*(left+right)*1.0)
            left-= TRIM_STEP
            right+= TRIM_STEP
            Run(mL,mR,left,right)
            angl=int(0.3*(right-left))
            csv.run(angl)
            #time.sleep(TRIM_TIME)
            #csv.run(-angl)
            #left+= TRIM_STEP
            #right-= TRIM_STEP

         if ch == "k" :
            #TRIM_STEP=int(0.5*(left+right)*1.0)
            left+= TRIM_STEP
            right-= TRIM_STEP
            Run(mL,mR,left,right)
            angl=int(0.3*(right-left))
            csv.run(angl)
            #time.sleep(TRIM_TIME)
            #csv.run(-angl)
            #left-= TRIM_STEP
            #right+= TRIM_STEP

         if ch == "l" :
            HANDLE_STEP=int(0.5*(left+right)*2.0)
            left+= HANDLE_STEP
            right-= HANDLE_STEP
            Run(mL,mR,left,right)
            time.sleep(HANDLE_TIME)
            left-= HANDLE_STEP
            right+= HANDLE_STEP

         if ch == "h" :
            HANDLE_STEP=int(0.5*(left+right)*2.0)
            left-= HANDLE_STEP
            right+= HANDLE_STEP
            Run(mL,mR,left,right)
            time.sleep(HANDLE_TIME)
            left+= HANDLE_STEP
            right-= HANDLE_STEP



         if ch == "f" :
            left+= STEP
            right+= STEP
         if ch == "g" :
            left+= 2*STEP
            right+= 2*STEP

         if ch == "d" :
            left-= STEP
            right-= STEP
         if ch == "s" :
            left-= 2*STEP
            right-= 2*STEP

         Run(mL,mR,left,right)

         time.sleep(SLEEP)

      except KeyboardInterrupt:
         mL.run(0)
         mR.run(0)
         csv.run(0)
         break

   print("\nTidying up")
   mL.run(0)
   mR.run(0)
   csv.run(0)
