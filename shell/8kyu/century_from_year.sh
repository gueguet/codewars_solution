#!/bin/bash

# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097

year=$1

century=$(($year/100))
reste=$(($year%100))

if [ $reste -eq 0 ]
then
  echo $century
else
  century=$((century+1))
  echo $century
fi
