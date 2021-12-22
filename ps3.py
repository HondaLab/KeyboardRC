import pygame
from pygame.locals import *

# ジョイスティックの初期化
pygame.joystick.init()
try:
   # ジョイスティックインスタンスの生成
   joystick = pygame.joystick.Joystick(1)
   joystick.init()
   print('ジョイスティックの名前:', joystick.get_name())
   print('ボタン数 :', joystick.get_numbuttons())
except pygame.error:
   print('ジョイスティックが接続されていません')

# pygameの初期化
pygame.init()

# 画面の生成
screen = pygame.display.set_mode((320, 320))

# ループ
active = True
count=0
while active:
   # イベントの取得
   for e in pygame.event.get():
       # 終了ボタン
       if e.type == QUIT:
           active = False

       # ジョイスティックのボタンの入力
       if e.type == pygame.locals.JOYAXISMOTION:
           count+=1
           #print(count, joystick.get_axis(0), joystick.get_axis(1))
           print("\r %d %10.7f %10.7f %10.7f %10.7f" % (count, joystick.get_axis(0), joystick.get_axis(1), joystick.get_axis(3), joystick.get_axis(4)),end='')
       '''
       elif e.type == pygame.locals.JOYBUTTONDOWN:
           print('ボタン'+str(e.button)+'を押した')
       elif e.type == pygame.locals.JOYBUTTONUP:
           print('ボタン'+str(e.button)+'を離した')
       '''

   #print(e)
