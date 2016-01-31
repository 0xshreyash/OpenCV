# Importing the numpy library 
import numpy as np
# Importing the opencv library
import cv2

img = cv2.imread('cr7.jpg', -1)
# -1 is for unchanged

cv2.imshow('Displaying cr7.img', img)

k = cv2.waitKey(0)

cv2.destroyAllWndows()


