#!/usr/bin/env python3
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("ColorImage.py /path/to/image")
        exit(1)
    img = cv2.imread(path,0)
    ret,thresh1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
    ret,thresh21 = cv2.threshold(img,27,255,cv2.THRESH_BINARY)
    ret,thresh22 = cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)
    thresh2= thresh21 & thresh22
    ret,thresh3 = cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    img = cv2.medianBlur(img,5)
    thresh4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    titles = ['Original Image','BINARY','Band Thresholding',"Semi Thresholding", 'Adaptive Gaussian Thresholding']
    images = [img, thresh1, thresh2, thresh3, thresh4]

    for i in range(5):
        plt.subplot(5,1,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()


