#!/usr/bin/bash


if (( $( echo "$1 >= -0.9" |bc -l) )) 
then
  echo "yes"
else
  echo "no"
fi
