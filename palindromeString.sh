#!/bin/bash
echo "Enter string here:"
read -r strlength=${#str}
isPalindrome=1
for (( l=0, r=length-1; l<r; l++, r-- )); do
    if [ "${str:l:1}" != "${str:r:1}" ]; then
        isPalindrome=0
        break
    fi
done

if [ $isPalindrome -eq 1 ]; then
    echo "Palindrome"
else
    echo "Not a Palindrome"
fi