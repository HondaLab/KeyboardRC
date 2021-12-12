# Keyboard RC
RasPiロボット(SSRX)で，ラジコンで操縦するプログラムです．
コントローラーは用いず，簡便にキーボードだけで，
前進，後退，右折，左折などを行います．

## Piカメラの向きを距離センサで制御
実行プログラム：ssr101b.py 
制御のアルゴリズムは modules/rc3c.py 内のKeyAssignクラスupdateメソッドの中に．

tofセンサーを４つ搭載した．
対応表

|ssr101b |tofL | tofR | tofC | tofM |
---------|-----|------|------|------|
|vl53_6a |tof1 | tof2 | tof3 | tof4 |
---------|-----|------|------|------|
|gpio    |22   |  4   | 17   |  27  |

## GPIOの変更
SSR2.1/3.1 でGPIOを大幅に変更する．
基盤上のピン配置と配線スペースの都合上．


motorL:23; motorR:14
camera servo:18

(2021 11/24)

## 必要なもの (Requirement)
### pigpiod
```
sudo apt-get install pigpiod
sudo pigpiod
```

### OpenCV
```
sudo apt-get install python3-opencv
```

## rcXX.pyを実行してください．
```
python3 rcXY.py
```

## キーボードで操縦します (Control by keyboard)

  - q: 終了
  - s: stop
  - f: 前進増速
  - d: 後退増速
  - j: 左折増速
  - k: 右折増速
  - h: 左折
  - l: 右折


