#!/bin/bash

base=$1
factor=$2

if [ `echo "$base % $factor" | bc` -eq 0 ]
then
  echo true
else
  echo false
fi


# * clever
(( base % factor )) && echo "false" || echo "true"
