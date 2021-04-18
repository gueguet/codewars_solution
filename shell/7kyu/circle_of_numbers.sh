#!bin/bash

# https://www.codewars.com/kata/58841cb52a077503c4000015/train/shell

n=$1
first_number=$2

if [ $first_number -lt $((n/2)) ];
    then
        echo $(($first_number + $n/2))
    else
        echo $(($first_number - $n/2))
fi