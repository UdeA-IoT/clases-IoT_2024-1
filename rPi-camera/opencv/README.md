
# Opencv

En construcción...

* OpenCV is a simple and powerful programming framework for computer vision. It is preferred by both novices and experts in the field of computer vision.
* OpenCV (also known as Open Source Computer Vision) is an open source library
for computer vision and machine learning. It has many functionalities for image
processing and computer vision. It is a cross-platform library, and it works with many
programming languages and OSes. It has a large collection of computer vision and
machine learning-related functions. It also has several Graphical User Interface (GUI)
and event handling features.
* It runs on a variety of OSes, including Windows, Android,
Linux, macOS, and other Unix-like OSes. In this book, we will write computer
vision-related programs with OpenCV and Python 3.
* As we will be writing computer vision programs with Raspberry Pi as the platform, we
will study single-board computers and Raspberry Pi in detail. We will learn how to set up
the Raspbian OS on various models of a Raspberry Pi single-board computer.


### Image datasets

We will need sample images for our computer vision programs with Python and OpenCV.
We can find a lot of images online. However, many of those images are under copyright.
Most computer vision researchers and professionals use standard image datasets. We
prefer to use the following image datasets all the time:
* http://sipi.usc.edu/database/
* https://www.imageprocessingplace.com/root_files_V3/image_databases.htm
* https://en.home.cvlab.cs.tsukuba.ac.jp/
* 



## Instalación



```bash
# Actualizar paquetes
sudo apt-get update
sudo apt-get upgrade
# Instalar prerequisitos
sudo apt install libatlas3-base
sudo apt install python3-numpy
sudo apt install python3-matplotlib
# Instalar opencv
sudo apt install python3-opencv
```

## Verificación de la instalación

```bash
$ python3
Python 3.9.2 (default, Mar 12 2021, 04:06:34) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> cv2.__version__
'4.5.1'
>>> exit()
```


**Nota**: Mirar si pillow esta, sino instalarlo tambien.



## Referencias
* https://www.waveshare.com/wiki/RPi_IR-CUT_Camera#raspicam_User_Guide
* https://picamera.readthedocs.io/en/release-1.13/
* https://raspberrypi-guide.github.io/programming/install-opencv
* https://programarfacil.com/blog/vision-artificial/opencv-raspberry-pi/
* https://raspberrytips.com/install-opencv-on-raspberry-pi/
* https://github.com/iotJumpway/RPI-Examples/blob/master/_DOCS/2-Installing-OpenCV-3-2-0.md
* https://learn.circuit.rocks/introduction-to-opencv-using-the-raspberry-pi
* https://learn.littlebirdelectronics.com.au/raspberry-pi/set-up-opencv-on-raspberry-pi-4
* https://learn.littlebirdelectronics.com.au/categories/raspberry-pi
* https://learn.littlebirdelectronics.com.au/
* https://learn.littlebirdelectronics.com.au/guides/create-a-noobs-microsd-card
* https://learn.littlebirdelectronics.com.au/guides/make-a-smart-aquarium
* https://learn.littlebirdelectronics.com.au/guides/temperature-and-humidity-sensor-with-raspberry-pi
* https://learn.littlebirdelectronics.com.au/guides/build-a-raspberry-pi-security-camera
* https://learn.littlebirdelectronics.com.au/guides/passive-infrared-sensor-with-raspberry-pi
* https://learn.littlebirdelectronics.com.au/guides/coronavirus-monitor-with-raspberry-pi
* https://learn.circuit.rocks/
* https://github.com/BrandonJoffe/home_surveillance
* https://github.com/deeptibhegde/Real-Time-Multiple-Person-Recognition-and-Tracking-for-CCTV-Camera
* https://github.com/Akash-Rayhan/Face_Recognition_System
* https://github.com/SharpAI/DeepCamera
* https://github.com/kunalyelne/Face-Recognition-using-Raspberry-Pi
* https://github.com/justsaumit/opencv-face-recognition-rpi4
* https://github.com/po1ar/Raspberry-Pi-Facial-Recognition-w-GUI
* https://medium.com/@shubhranshumalhotra/face-recognition-security-system-on-home-security-cameras-using-python-diary-part-1-14946cec83c1
* https://pyimagesearch.com/2019/12/02/opencv-vehicle-detection-tracking-and-speed-estimation/
  
