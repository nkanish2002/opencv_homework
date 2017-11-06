#!/usr/bin/env python3
import cv2
import sys
import copy
import numpy as np
import os
import sys
from matplotlib import pyplot as plt


def add_gauss(image,mean,sigma):
	gauss = np.random.normal(mean,sigma,(image.shape[0],image.shape[1]))
	gauss = gauss.reshape(image.shape[0],image.shape[1])
	noisy = image + gauss
	return noisy

def noise_snp(image,pa,pb):
	result = np.copy(image)

	n_s = np.ceil(image.size * pa)
	c_s = [np.random.randint(0, i-1, int(n_s)) for i in image.shape]
	result[c_s] = 255

	n_p = np.ceil(image.size * pb)
	c_p = [np.random.randint(0, j-1, int(n_p)) for j in image.shape]
	result[c_p] = 0
	return result

if __name__ == "__main__":
	if len(sys.argv) > 1:
		path = sys.argv[1]
	else:
		print("ColorImage.py /path/to/image")
		exit(1)
	image = cv2.imread(path, 0)
	g_image = add_gauss(image,5,20 )
	snp_image = noise_snp(image,0.03,0.03)
	kernel = (7,7)
	g_box = cv2.blur(g_image,kernel)
	snp_box = cv2.blur(snp_image,kernel)
	g_gauss = cv2.GaussianBlur(g_image,kernel,0)
	snp_gauss = cv2.GaussianBlur(snp_image,kernel,0)
	g_median = cv2.medianBlur(g_image.astype(np.uint8),kernel[0])
	snp_median = cv2.medianBlur(snp_image.astype(np.uint8),kernel[0])
	
	titles = ['Original Image','Gaussian','Salt and paper','Gauss Box Filter','Salt and Pepper Box Filter','Gauss Gaussian Filter','Salt and Pepper Gaussian Filter', 'Gauss Median Filter','Salt and Pepper Median Filter']
	images = [image, g_image, snp_image, g_box, snp_box, g_gauss, snp_gauss, g_median , snp_median]
	
	for i in range(9):
		plt.subplot(5,2,i+1),plt.imshow(images[i],'gray')
		plt.title(titles[i])
		plt.xticks([]),plt.yticks([])

	plt.show()
		