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

def mosaic(img, new_order, first_index_is_zero=False):
    rows, cols, *_ = new_order.shape
    dy = img.shape[0] // rows # height of each mosaic cell
    dx = img.shape[1] // cols # width of each mosaic cell
    
    if not first_index_is_zero:
        new_order -= 1
    
#     print(img.shape)
#     mosaic = img.reshape((rows, dy, cols, dx, -1));     print(mosaic.shape)
#     mosaic = mosaic.swapaxes(1, 2);                     print(mosaic.shape)
#     mosaic = mosaic.reshape((rows * cols, dy, dx, -1)); print(mosaic.shape)
#     mosaic = mosaic[new_order] # reorder the mosaic cells
#     mosaic = np.hstack(mosaic);                         print(mosaic.shape)
#     mosaic = np.hstack(mosaic);                         print(mosaic.shape)
#     mosaic = mosaic.reshape((*img.shape));              print(mosaic.shape)
#     return mosaic

    return (
        np.hstack(
            np.hstack(
                img
                    .reshape((rows, dy, cols, dx, -1))  # (512, 512)          -> (4, 128, 4, 128, 1)
                    .swapaxes(1, 2)                     # (4, 128, 4, 128, 1) -> (4, 4, 128, 128, 1)
                    .reshape((rows * cols, dy, dx, -1)) # (4, 4, 128, 128, 1) -> (16, 128, 128, 1)
                    [new_order]                         # reorders the mosaic cells
            )                                           # (16, 128, 128, 1)   -> (4, 512, 128, 1)
        )                                               # (4, 512, 128, 1)    -> (512, 512, 1)
        .reshape((*img.shape)))                         # (512, 512, 1)       -> (512, 512)


img = mosaic(data[1], np.array([6,11,13,3,8,16,1,9,12,14,2,7,4,15,10,5]).reshape((4,4)))
plotAndSave(img, "mosaico")