#!bin/bash

# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/shell

res=""

# be careful do not used "" around $1 here --> need to iterate through each word!
for word in $1;
do 
    res=$"$word $res"
done
echo $res
