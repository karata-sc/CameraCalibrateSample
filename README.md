# CameraCalibrateSample
---
パラメータの取得
---

１．必要なパッケージをインストール

```
$ sudo apt install ros-noetic-usb-cam
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


```
$ rosrun usb_cam usb_cam_node
[ INFO] [1633934648.926744583]: using default calibration URL
[ INFO] [1633934648.927417750]: camera calibration URL: file:///home/owner/.ros/camera_info/head_camera.yaml
[ INFO] [1633934648.927505186]: Unable to open camera calibration file [/home/owner/.ros/camera_info/head_camera.yaml]
[ WARN] [1633934648.927534265]: Camera calibration file /home/owner/.ros/camera_info/head_camera.yaml not found.
[ INFO] [1633934648.927563539]: Starting 'head_camera' (/dev/video0) at 640x480 via mmap (mjpeg) at 30 FPS
[ WARN] [1633934649.107271801]: unknown control 'focus_auto'
```
指定されたディレクトリ（この場合 ~/.ros/camera_info/head_camera.yaml）にキャリブレーションのファイルを入れることでusb_cam_nodeの起動と一緒にキャリブレーションをしてくれる．

これを使うにはパラメータのファイルが必要．カメラキャリブレーションのプログラムを実行した後，CALIBLATEの下のSAVEボタンを押すと/tmpにアーカイブファイルがcalibrationdata.tar.gzという名前で保存される．
以降の操作↓
```
$ cd /tmp
$ tar zxvf calibrationdata.tar.gz
$ mv ost.txt ost.ini 
$ rosrun camera_calibration_parsers convert ost.ini head_camera.yaml
```

ここで，~/.ros/camera_infoが存在しない場合は作っておく．

```
$ cd ~/.ros
$ mkdir camera_info
$ mv /tmp/head_camera.yaml ~/.ros/camera_info/head_camera.yaml
```

```
$ cd camera_info
$ vi head_camera.yaml
```
camera_nameをusb_cam_nodeが起動した時に出るアドレスに変更する

自分の場合はcamera_name: narrow_stereoになっていたのでcamera_name: head_cameraに書き換えた




---
参考資料
---
* [カメラキャリブレーション — OpenCV-Python Tutorials 1 documentation](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_calib3d/py_calibration/py_calibration.html)

* [中込 広幸 (Hiroyuki Nakagomi) - 研究ブログ - researchmap](https://researchmap.jp/blogs/blog_entries/view/96639/ba1ff72ca68727e9e2b828cbf8b30e9e?frame_id=461924)


