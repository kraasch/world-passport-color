import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

if len(sys.argv) != 9:
    print("Usage: <script>.py <in_file>.png <out_file>.png <r> <g> <b> <x> <y> <pointer_flag>(0=hide)")
    exit(0)

imageFile=sys.argv[1]
outFile=sys.argv[2]
r_color=sys.argv[3]
g_color=sys.argv[4]
b_color=sys.argv[5]
x_coord=sys.argv[6]
y_coord=sys.argv[7]
pt_flag=sys.argv[8]
img = cv2.imread(imageFile, cv2.IMREAD_COLOR) # reads probably as BGR.

h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
seed_pt = (int(x_coord),int(y_coord))
fixed_range = True
connectivity = 4
color=(int(b_color), int(g_color), int(r_color)) 

flooded = img.copy()
mask[:] = 0
lo=100
hi=255
flags = connectivity
if fixed_range:
    flags |= cv2.FLOODFILL_FIXED_RANGE
cv2.floodFill(flooded, mask, seed_pt, color, (lo,)*3, (hi,)*3, flags)
if int(pt_flag) != 0:
    cv2.circle(flooded, seed_pt, 2, (0, 0, 255), -1)
cv2.imwrite(outFile, flooded)

# sources .
# https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html#floodfill
# https://github.com/npinto/opencv/blob/master/samples/python2/floodfill.py
# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=gettrackbarpos#cv2.getTrackbarPos
