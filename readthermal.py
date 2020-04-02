import serial
import numpy as np


ser = serial.Serial("/dev/ttyACM0", 115200)


def getData():
	frames = 0;
	while True:
		frames+=1
		recv = ser.readline()
		recv = recv.rstrip() #strip the return character
		if(frames > 1):#ditch the first frame in case it is incomplete
			data = np.fromstring(recv, dtype=float, count=-1, sep=',') #get the data
			print(data)


try:
	if ser.is_open == False:
		ser.open()
	getData()
except KeyboardInterrupt:   # Ctrl+C
	if ser != None:
		ser.close()
