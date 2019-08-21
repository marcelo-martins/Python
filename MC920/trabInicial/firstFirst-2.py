import cv2;
import numpy as np;
import math

import os
import glob

#Trying to get all my images using a quora solution
image_dir = "/home/marcelomartins/Documentos/Python/MC920/trabInicial/images"
data_path = os.path.join(image_dir, '*g')
files = glob.glob(data_path)
data=[]
for fl in files:
    img = cv2.imread(fl, cv2.IMREAD_GRAYSCALE)
    data.append(img)

im_in = data[5]

cv2.imshow("Original", im_in)
cv2.waitKey(0)

gamma = 4.5

#First: convert from [0,255] -> [0,1]
#Then, apply B=A^(1/gamma) to this range of values
#Convert back [0,1] -> [0,255]
#The bigger the chosen gamma value, the brighter your image will be
for x in range(0, im_in.shape[0]):
    for y in range(0, im_in.shape[1]):
        im_in[x,y] = int(255*math.pow(im_in[x,y]/255, (1.0/gamma)))

cv2.imshow("Bright", im_in)
cv2.waitKey(0)