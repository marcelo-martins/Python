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

img_A = data[4]
img_B = data[2]


cv2.imshow("A", img_A)
cv2.waitKey(0)
cv2.imshow("B", img_B)
cv2.waitKey(0)

print(img_A.shape[0])
print(img_B.shape)

x1 = 0.8
x2 = 1-x1

#supposing that they have the same size
# for x in range(0, img_A.shape[0]):
#     for y in range(0, img_A.shape[1]):
#         img_out[x,y] = int(x1 * img_A[x,y] + x2 * img_B[x,y])

# cv2.imshow("Compose", img_out)
# cv2.waitKey(0)

img_out = x1*img_A + x2*img_B
plotAndSave(img_out, f"Compose_{x1}_{x2}")