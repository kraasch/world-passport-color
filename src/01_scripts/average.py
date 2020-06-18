import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

if len(sys.argv) != 2:
    print("Usage: <script>.py <image_file>.png")
    exit(0)

imageFile=sys.argv[1]
image = cv2.imread(imageFile, cv2.IMREAD_COLOR) # reads probably as BGR.

w,h,c=image.shape
#print('Original: width--' + str(w) + ', height--' + str(h) + ', channels--' + str(c) + '.')

chan_num=(0,1,2)
chan_col=('blue ', 'green', 'red  ')
avgz=[]

for i in chan_num:
    chanImg=image[:,:,i]
    chanSum=np.sum(chanImg)
    w,h=chanImg.shape
    chanSize=w*h
    chanAvg=chanSum/chanSize
    #print(chan_col[i] + ':  sum--' + str(chanSum) + ', size--' + str(chanImg.shape) + '=' + str(chanSize) + ', average--' + str(chanAvg) + '.')
    avgz.append(chanAvg)

print(int(avgz[2]),int(avgz[1]),int(avgz[0])) 

# sources .
# https://note.nkmk.me/en/python-opencv-pillow-image-size/
# https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv

