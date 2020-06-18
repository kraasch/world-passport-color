#!/usr/bin/env bash

skip=0
if $(test -n "$@"); then
  skip="$@"
fi

cat ../data/regions_coordinates.txt > inputCoordinates.txt
cp ./test.png.tmp ./test.png

echo "_______________________________" >> ./removeTheseCoordinates.txt

while read -r -u 3 x; do

  if $(test $skip -ge 0); then
    skip=$(($skip - 1))
    continue
  fi

  x=$(echo "$x" | tr -d '[' | tr -d ']' | tr -d ',' | tr -d "'")
  cid=$(echo "$x" | awk '{print $1}') # country id .
  xPt=$(echo "$x" | awk '{print $2}')
  yPt=$(echo "$x" | awk '{print $3}')

  y=$(cat ../data/country_colors.csv | grep "$cid" | sed 's/...//')
  rCol=$(echo "$y" | awk '{print $1}')
  gCol=$(echo "$y" | awk '{print $2}')
  bCol=$(echo "$y" | awk '{print $3}')

  cat ../data/country_names.csv | grep "${cid};"
  echo "$x ---> ($y)"

  python3 makeFill.py test.png out.png "$rCol" "$gCol" "$bCol" "$xPt" "$yPt" 0

  sxiv ./out.png
  echo "RET key to apply change. (Y/n)"
  read applyChange
  if $(test -z "$applyChange"); then
    mv ./out.png ./test.png
  else
    echo "$x ---> ($y)" >> ./removeTheseCoordinates.txt
  fi
done 3< inputCoordinates.txt 

sxiv ./test.png

