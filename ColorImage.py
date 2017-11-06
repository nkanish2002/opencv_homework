#!/usr/bin/env python3
import sys
import cv2
import numpy as np

def split_into_channels(image):
	ch3 = image[:,:,2]
	ch2 = image[:,:,1]
	ch1 = image[:,:,0]
	return ch1, ch2, ch3

if __name__ == "__main__":
	if len(sys.argv) > 1:
		path = sys.argv[1]
	else:
		print("ColorImage.py /path/to/image")
		exit(1)
	image = cv2.imread(path,cv2.IMREAD_COLOR)
	#image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	#image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

	ch1,ch2,ch3 = split_into_channels(image)
	for values, channel in zip((ch1,ch2,ch3), (2,1,0)):
		img = np.zeros((values.shape[0], values.shape[1], 3), dtype = values.dtype) 
		img[:,:,channel] = values
		print(int(img[20,25,1]))
		cv2.imshow('Image',img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	#cv2.imshow('Image',image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
