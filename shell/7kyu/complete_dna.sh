#!/bin/bash

# https://www.codewars.com/kata/complementary-dna/shell

i=1
c=""

# * args looks like ['ATTAT']
# * weird but the ' is not taken into account in the loop
while [ $i -le ${#1} ]
do
	var=$(echo $1 | cut -c $i) # extract one caracther (c = column)
	if [ $var == "A" ]
	then
		x="T"
	elif [ $var == "T" ]
	then
		x="A"
	elif [ $var == "C" ]
	then
		x="G"
	elif [ $var == "G" ]
	then
		x="C"
	fi
	c="$c$x"
	((i++))
done

echo "${c}"