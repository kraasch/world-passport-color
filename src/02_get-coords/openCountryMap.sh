#!/usr/bin/env bash

skip=0
if $(test -n "$@"); then
  skip="$@"
fi

while read -r -u 3 x; do 

  if $(test $skip -ge 0); then
    skip=$(($skip - 1))
    continue
  fi

  name=$(echo "$x" | sed 's/...//' | tr '_' ' ')
  echo Now at "https://nominatim.openstreetmap.org/search.php?polygon_geojson=1&viewbox=&q=$name ($x)"
  xdg-open "https://nominatim.openstreetmap.org/search.php?polygon_geojson=1&viewbox=&q=$name"
  read y

done 3< ./country_names.csv

