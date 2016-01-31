# Importing the numpy library 
import numpy as np
# Importing the opencv library
import cv2

img = cv2.imread('cr7.jpg', -1)
# -1 is for unchanged

# sequence of numbers 
print(img)