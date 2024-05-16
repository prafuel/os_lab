#!/bin/bash
isPrime=1
read -p "Enter number here : " num

for (( i=2; i<=num/2; i++ ))
do
    if [ $((num % i)) -eq 0 ] 
    then
        isPrime=0
    break   
    fi
done

if [ $isPrime -eq 1 ] 
then
    echo "Prime Number"
else
    echo "Non Prime"
fi