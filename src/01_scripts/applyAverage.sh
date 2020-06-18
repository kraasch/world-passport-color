#!/usr/bin/env bash

for x in images_thumbs/*; do
  printf "$x;"
  python3 average.py "$x"
done > outColors.csv

