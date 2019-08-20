import cv2;
import numpy as np; 

im_in = cv2.imread("insta.png", cv2.IMREAD_COLOR);

cv2.imshow("Foi?", im_in);
cv2.waitKey(0)