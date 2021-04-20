#!bin/bash

# https://www.codewars.com/kata/56484848ba95170a8000004d/train/shell

gps() {

    time_array=($(echo "$2" | tr ',' '\n'))

    for i in "${time_array[@]}"
    do
        echo $i
    done

}
gps $1 "$2"
