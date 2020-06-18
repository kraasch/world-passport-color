#!/usr/bin/env bash

cat coordinates.txt |
  tr -d ',' |
  tr -d ']' |
  tr -d '[' |
  tr -d "'" |
  tr ' ' ';' > ../data/new.txt

rm coordinates.txt
