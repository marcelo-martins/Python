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


#1.1Negativ of an image
#im_in = cv2.imread("/home/marcelomartins/....", cv2.IMREAD_GRAYSCALE); way of reading 
im_in = data[5]

cv2.imshow("Original", im_in);
cv2.waitKey(0)

#another way: im_negativ = 255 - im_in
im_negativ = im_negativ = cv2.bitwise_not(im_in)
cv2.imshow("Inverted", im_negativ)
cv2.waitKey(0)

#Save image: name, image you want to save
#cv2.imwrite('messigray.png',img)


#1.2 adjust [0,255] to [100, 200]

for x in range(0, im_in.shape[0]):
    for y in range(0, im_in.shape[1]):
        im_in[x,y] = int(float(im_in[x,y]/2.55) + 100)
        print(im_in[x,y])
        if(y==252):
            break 

cv2.imshow("different range", im_in)
cv2.waitKey(0)