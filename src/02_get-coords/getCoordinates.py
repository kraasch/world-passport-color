#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import pandas as pd

codes=[]
names=[]

my_csv = pd.read_csv('./country_names.csv', sep=';', names=('codes', 'names'))
codes = my_csv.codes.to_numpy()
names = my_csv.names.to_numpy()

i=0
codeMax=len(codes)-1

if len(sys.argv) != 2:
    print("Usage: <script>.py <in_file>.png")
    exit(0)

imageFile=sys.argv[1]
img = cv2.imread(imageFile, cv2.IMREAD_COLOR) # reads probably as BGR.
mouseX=None
mouseY=None

def draw_circle(event, x, y, flags,param):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        circ_width_px=1
        circ_width_fill=-1
        circ_color=(255,0,0)
        circ_diameter1=10
        circ_diameter2=2
        cv2.circle(img, (x, y), circ_diameter1, circ_color, circ_width_px)
        cv2.circle(img, (x, y), circ_diameter2, circ_color, circ_width_fill)
        mouseX, mouseY = x, y

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
coords=[]

def printStatus():
    global codes
    global names
    print('Currently at code: ' + codes[i] + ', name: ' + names[i])

def printHelp():
    print("'h'  -- print help.")
    print("'l'  -- show list of all added coordinates.")
    print("'d'  -- delete last added coordinates.")
    print("'p'  -- go to previous country code.")
    print("'n'  -- go to next country code.")
    print("'a'  -- add a coordinate for the current country code.")
    print("'q'  -- quit, and save country codes.")

printStatus()
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF

    if k == 27 or k == ord('q'): # Exit on ESC key or q key.
        break

    elif k == ord('h'): # list all elements
        printHelp()
        continue

    elif k == ord('l'): # list all elements
        print(coords)
        continue

    elif k == ord('d'): # delete last element.
        printStatus()
        if len(coords) > 0:
            print('Deleting ' + str(coords[len(coords)-1]))
            coords = coords[:-1]
        else:
            print('Nothing to delete.')
        continue

    elif k == ord('p'): # move to previous country code.
        i=max(0, i-1)
        printStatus()
        continue

    elif k == ord('n'): # move to next country code.
        i=min(codeMax, i+1)
        printStatus()
        continue

    elif k == ord('a'): # add last click's coordinates to console.
        val=[codes[i], mouseX, mouseY]
        print(str(val))
        coords.append(val)

with open('coordinates.txt', 'w') as f:
    for item in coords:
        f.write("%s\n" % item)

# sources .
# https://stackoverflow.com/questions/28327020/opencv-detect-mouse-position-clicking-over-a-picture
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
