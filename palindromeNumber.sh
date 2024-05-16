#!/bin/bash
read -p "Enter number to check, is it palindrome or not: " num
copy=$num
newValue=0

# Reverse the number
while [ $copy -ne 0 ]; do
    rem=$((copy % 10))
    newValue=$((newValue * 10 + rem))
    copy=$((copy / 10))
done

echo "Reverse number : $newValue"

if [ $newValue -eq $num ]; then
    echo "Palindrome number"
else
    echo "Non Palindrome Number"
fi