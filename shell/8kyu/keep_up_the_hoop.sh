#!/bin/bash

# https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145/train/shell

function hoopCount () {
  n=$1
  if [ $n -ge 10 ]
  then 
    echo "Great, now move on to tricks"
  else
    echo "Keep at it until you get it"
  fi
}

hoopCount $1


: '
solution nice to know :

win="Great, now move on to tricks";
fail="Keep at it until you get it";

[[ $1 -ge 10 ]] && echo $fail || echo $win;
'