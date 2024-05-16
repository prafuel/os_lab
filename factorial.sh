#!/bin/bash
read -p "Enter Number : " num
fact=1
for ((i=1; i<=$num; i++))
do
fact=$((fact * i))
done
echo "Factorial Is : $fact"