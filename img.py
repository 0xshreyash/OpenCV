import numpy as np
import cv2

# 0 is for saving the image as a grayscale image
img = cv2.imread('cr7.jpg',0)

# displaying image
cv2.imshow('image',img)

#waiting for a key to be pressed indefinitely
k = cv2.waitKey(0) & 0xFF

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('cr7gray.png',img)
    cv2.destroyAllWindows()