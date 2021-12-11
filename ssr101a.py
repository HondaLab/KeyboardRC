#!/usr/bin/python3

# ssr101a.py
# Yasushi Honda 2021 12/3

# How to execute
# sudo pigpiod
# pyhton3 ssrXY.py 

import modules.keyin as keyin # キーボード入力を監視するモジュール
import modules.rc3b as rc
import modules.vl53_6a as tof
import time
import numpy as np

SLEEP=0.1
PERIOD=0.3
ssr3=rc.KeyAssign()
tofL,tofR,tofC,tofM=tof.start()

key = keyin.Keyboard()
ch="c"
print("##################################")
print("Input q to stop.")
print("left,right,distL,distC,distR,distM")
now=time.time()
init=now
start=now
while ch!="q":
   ch = key.read()
   try:
      left,right=ssr3.update(ch)
      distL=tofL.get_distance()
      distR=tofR.get_distance()
      distC=tofC.get_distance()
      distM=tofM.get_distance()
      now=time.time()
      if now-start>PERIOD:
         print("\r %4d %4d %5d %5d %5d %5d" % (left,right,distL,distC,distR,distM),end='')
         start=now
      #time.sleep(SLEEP)
   except KeyboardInterrupt:
      ssr3.stop()
      break

print("\n Bye Bye!")
ssr3.stop()
