import cv2
import numpy
import os

randomArray = bytearray(os.urandom(120000))

flatNumpyArray = numpy.array(randomArray)

grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGrayImage.png', grayImage)
colorImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColorImage.png', colorImage)