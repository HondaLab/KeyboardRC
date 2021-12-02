#!/usr/bin/python3

# ssr109a.py
# Yasushi Honda 2021 9/3

# How to execute
# sudo pigpiod
# pyhton3 rcXY.py 

import modules.keyin as keyin # キーボード入力を監視するモジュール
import modules.rc3b as rc
import modules.vl53_4a as tof
import time
import numpy as np

SLEEP=0.1
ssr3=rc.KeyAssign()
tofL,tofR,tofC=tof.start()

key = keyin.Keyboard()
ch="c"
print("Input q to stop.")
while ch!="q":
   ch = key.read()
   try:
      left,right=ssr3.update(ch)
      distL=tofL.get_distance()
      distR=tofC.get_distance()
      distC=tofR.get_distance()
      safe=np.tanh(1.0*(distC-100))
      print("\r %4d %4d %5d %5d %5d" % (left,right,distL,distC,distR),end='')
      #time.sleep(SLEEP)
   except KeyboardInterrupt:
      ssr3.stop()
      break

print("\n Bye Bye!")
ssr3.stop()
