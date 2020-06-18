import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

if len(sys.argv) != 2:
    print("Usage: <script>.py <image_file>.png")
    exit(0)

imageFile=sys.argv[1]
image = cv2.imread(imageFile, cv2.IMREAD_COLOR) # reads probably as BGR.
ret, thresh=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imwrite(imageFile+'_binary.png', thresh)

# sources .
# https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html

