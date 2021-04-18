#!/bin/bash

# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/shell

repeat=$1
string=$2

res=""

START=1
END=$repeat

for i in $(eval echo "{$START..$END}")
do
    res+=$string
done

echo $res


: '
* better solution
echo $(printf "%.s$2" $(seq $1))
'