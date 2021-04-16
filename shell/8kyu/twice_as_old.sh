#!/bin/sh

dad_years_old=$1
son_years_old=$2

diff_age=0

# check if 2 * years old of son is > or < to dad yo
if [ $((son_years_old*2)) -gt $dad_years_old ]
then
    while [ $((son_years_old*2)) -ge $dad_years_old ]
    do
        if [ $dad_years_old -eq $((son_years_old*2)) ]
            then
            echo ${diff_age#-}
        fi
        ((son_years_old--))
        ((dad_years_old--))
        ((diff_age--))
    done

else
    while [ $((son_years_old*2)) -le $dad_years_old ]
    do
        if [ $dad_years_old -eq $((son_years_old*2)) ]
            then
            echo $diff_age
        fi
        ((son_years_old++))
        ((dad_years_old++))
        ((diff_age++))
    done
fi


: '
* could have been way shorter...
total=$((dad_years_old-2*son_years_old))
echo "${total#-}"
'