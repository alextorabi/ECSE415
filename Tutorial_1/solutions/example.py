## import required python package

import numpy as np
import cv2

## read the image
img = cv2.imread('Lenna_image.png')

## check shape of image
img.shape

## display image
cv2.imshow('image',img)
## infinitely wait for a user keypress
cv2.waitKey(5000000)
## close all windows
# cv2.destroyAllWindows()


