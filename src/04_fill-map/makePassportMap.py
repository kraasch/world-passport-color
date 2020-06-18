#!/usr/bin/env python3

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import sys
import cv2

imgFile='./test.png'
outFile='./fullMap.png'

csv1 = pd.read_csv('./../data/country_colors.csv', sep=';', names=('codes', 'rs', 'gs', 'bs'))
codes_color = csv1.codes.to_numpy()
rs = csv1.rs.to_numpy()
gs = csv1.gs.to_numpy()
bs = csv1.bs.to_numpy()

csv2 = pd.read_csv('./../data/regions_coordinates.txt', sep=';', names=('codes', 'myxs', 'myys'))
codes_coord = csv2.codes.to_numpy()
xs = csv2.myxs.to_numpy()
ys = csv2.myys.to_numpy()

img = cv2.imread(imgFile, cv2.IMREAD_COLOR) # reads probably as BGR.

def myFlood(img, r_color, g_color, b_color, x_coord, y_coord):

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
    return flooded

def findIndexes(arr, term):
    indexes = [i for i,x in enumerate(arr) if x == term]
    return indexes

img = myFlood(img,200,200,200,0,0) # color water black
for i in range(0, len(xs)):
    x=xs[i]
    y=ys[i]
    j=findIndexes(codes_color, codes_coord[i])
    img = myFlood(img, rs[j], gs[j], bs[j], x, y)
    num=('000' + str(i))[-3:]
    # outFile='out/' + num + '_out.png'
cv2.imwrite(outFile, img)

# sources
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

