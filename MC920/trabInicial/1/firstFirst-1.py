import cv2;
import numpy as np;
import math
import matplotlib.pyplot as plt
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

def plotAndSave(title = ""):  
    plt.axis("off")
    plt.title(title)
    plt.imshow(im_out, cmap="gray", vmin=0, vmax=255)

    plt.waitforbuttonpress(0)
    plt.close("all")

    cv2.imwrite(title+".png", im_out)


#1.1Negativ of an image
#im_in = cv2.imread("/home/marcelomartins/....", cv2.IMREAD_GRAYSCALE); way of reading 
im_in = data[2]

cv2.imshow("Original", im_in)
cv2.waitKey(0)

#another way: im_negativ = 255 - im_in
im_negativ = im_negativ = cv2.bitwise_not(im_in)
cv2.imshow("Inverted", im_negativ)
cv2.waitKey(0)


#1.2 adjust [0,255] to [100, 200]

#with loops

# for x in range(0, im_in.shape[0]):
#     for y in range(0, im_in.shape[1]):
#         im_in[x,y] = int(float(im_in[x,y]/2.55) + 100)

# cv2.imshow("different range", im_in)
# cv2.waitKey(0)

#without loops
im_out = im_in/2.55 + 100
title = "[100, 200]"
plotAndSave(title)