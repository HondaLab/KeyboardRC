#!/usr/bin/python3

# ssr3ps3.py recieve controll data from ps3
# Yasushi Honda 2021 12/23

# How to execute
# sudo pigpiod
# pyhton3 ssrXY.py 

import modules.keyin as keyin # キーボード入力を監視するモジュール
import modules.rc3c as rc
import modules.vl53_6a as tof
import modules.socket as sk
import socket
import time
import numpy as np

SLEEP=0.1
PERIOD=0.3
ssr3=rc.KeyAssign()
tofL,tofR,tofC,tofM=tof.start()

udp=sk.UDP_Recv(sk.robot,sk.port)
data=[4]
key = keyin.Keyboard()
ch="c"
print("##################################")
print("Input q to stop.")
print("left,right,angl, distL,distC,distR,distM")
now=time.time()
init=now
start=now
while ch!="q":
   ch = key.read()
   try:
      data=udp.recv()
      distL=tofL.get_distance()
      distR=tofR.get_distance()
      distC=tofC.get_distance()
      distM=tofM.get_distance()
      dL=np.sqrt(distL*distC)
      dR=np.sqrt(distR*distC)
      left,right,angl=ssr3.update(ch,distL,distR)
      now=time.time()
      if now-start>PERIOD:
         print("\r %4d %4d %4d %5.2f %5.2f %5.2f %5.2f" % (left,right,angl,data[0],data[1],data[2],data[3]),end='')
         start=now
      #time.sleep(SLEEP)
   except (BlockingIOError, socket.error)
      pass

print("\n Bye Bye!")
ssr3.stop()
