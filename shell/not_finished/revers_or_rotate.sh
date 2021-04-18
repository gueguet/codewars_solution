#!bin/bash

# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/shell

# * done in python for now...

revrot () {

    main_string=$1
    chunk=$2

    sub_string=${main_string:0:$chunk}

    sum_cube=0
    for digit in $sub_string;
    do
        sum_cube+=$((digit**3))
    done
    echo $sum_cube
    # echo $sub_string


}





revrot $1 $2


