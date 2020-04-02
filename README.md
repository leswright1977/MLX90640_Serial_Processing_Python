# MLX90640_Serial_Processing_Python
Fast Python Processing script for serial data from an MLX90640 running on a Teensy 4.0

This is a Python version of MLXHeatCam.pde from https://github.com/sparkfun/SparkFun_MLX90640_Arduino_Example

MLXHeatcam is a little slow because of filter(BLUR,7); and I didn't really want to fire up an IDE to use the camera, so I rolled my own processing script in Python ad OpenCV.

I have the MLX90640 wired to a Teensy 4.0 running the original sparkfun "Output to Processing" script (edited, to give us 16FPS)

Serial Data is received by displaythermal.py (in src). This reads in the serial data, turns it into  numpy array and does some processing in OpenCV. Thermal data is cubic interpolated to give an impression of a higher resolution. The sensor is only 32 by 24 and is scaled to 320 by 240.

readthermal.py just shows raw numpy data in the console, if that is what you need!

![Screenshot](media/thermal.gif)

This should run on a RPi just fine (not tested yet) I intend to combine frames from the Picam as I did in onther project shortly!

Note: Both scripts assume the Teesny enumerates as: /dev/ttyACM0  You may have to change this!
