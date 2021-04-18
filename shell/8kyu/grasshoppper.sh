#!bin/bash

# https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/shell

position=$1
roll=$2

echo $(($position + $roll*2))