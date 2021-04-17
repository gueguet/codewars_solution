#!/usr/bin/bash

# ! disclaimer - not working... problem with float / round / int...

# https://www.codewars.com/kata/569b5cec755dd3534d00000f/train/shell

new_avg() {
    res=0
    sum_array=0
    len_array=0
    tot=0

    for i in $1;
    do
        ((len_array++))
        int=$(printf '%.*f\n' 0 $i)
        let tot+=$int
    done

    ((len_array++))
    res=$(echo "$len_array*$2 - $tot" | bc | awk '{print int($1+0.5)}')

    if [ $res -lt 0 ]
        then
        echo "ERROR" 
        else
        echo $res
    fi
}

new_avg "$1" $2


: '
* one solution :
new_avg() {
        arr=($(echo $1))
        let len=${#arr[@]}+1
        sum=$(echo ${arr[*]} | tr ' ' '\n' | awk 'BEGIN{sum=0}{sum=sum+$1}END{print sum}')
        last=$(echo "$len*$2-$sum" | bc)
        last=$((${last//.*/+1}))
        [ $last -le 0 ] && echo ERROR || echo $last
}
new_avg "$1" $2
'

