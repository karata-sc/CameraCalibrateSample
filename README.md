# CameraCalibrateSample
---
パラメータの取得
---

１．必要なパッケージをインストール

```
$ sudo  apt install ros-noetic-usb-cam
$ sudo apt install ros-noetic-camera-calibration
$ sudo apt install ros-noetic-image-proc 
```

２．roscoreを実行

```
$ roscore
```

３．カメラノード立ち上げ

```
$ rosrun usb_cam usb_cam_node
```
４．キャリブレーションプログラムの実行

```
$ rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.035 image:=/usb_cam/image_raw
```

---
キャリブレーションの反映
---
取得したパラメータの行列をサンプルプログラム`camera_calibration.py`の変数に代入する．
（５行目の`mtx`の値をcamera matrixに，８行目の`dist`の値をdistortionにそれぞれ書き換える．）


---
参考資料
---
* [カメラキャリブレーション — OpenCV-Python Tutorials 1 documentation](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_calib3d/py_calibration/py_calibration.html)
