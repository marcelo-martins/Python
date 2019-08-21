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

def plotAndSave(im_out, title = ""):  
    plt.axis("off")
    plt.title(title)
    plt.imshow(im_out, cmap="gray", vmin=0, vmax=255)

    plt.waitforbuttonpress(0)
    plt.close("all")

    cv2.imwrite(title+".png", im_out)

im_in = data[1]

for plane in range(0, 8):
    im_out = (im_in >> plane) & 1
    title = f"planoDeBit_{plane}"
    plotAndSave(np.where(im_out, 255, 0), title)
