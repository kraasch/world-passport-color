#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

r_color=100
g_color=100
b_color=100
x_coord=100
y_coord=100
seed_pt = (int(x_coord), int(y_coord))
color=(int(b_color), int(g_color), int(r_color)) 

img = cv2.imread('./world_v08_binary+edited.png', cv2.IMREAD_COLOR) 
h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
pts=[
        (100, 100),
        (100, 100),
        ]


flooded = img.copy()
mask[:] = 0
flags = 4
flags |= cv2.FLOODFILL_FIXED_RANGE
cv2.floodFill(flooded, mask, seed_pt, color, (100,)*3, (255,)*3, flags)
for pt in pts:
    cv2.circle(flooded, pt,  5, (0, 0, 255), 1)
    cv2.circle(flooded, pt, 10, (0, 0, 255), 2)
    cv2.circle(flooded, pt, 30, (0, 0, 255), 3)
cv2.imwrite('./out.png', flooded)

