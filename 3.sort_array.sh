#!/bin/bash

insertionSort() {
    local -n _arr=$1
    local n="${#_arr[@]}"
    for ((i = 1; i < n; i++)); do
        local key="${_arr[i]}"
        local j="$((i - 1))"
        while ((j >= 0 && _arr[j] > key)); do
            _arr[$((j + 1))]=${_arr[j]}
            ((j--))
        done
        _arr[$((j + 1))]=$key
    done
    eval "$1"=\( "${_arr[@]}" \)  # Update the original array
}

printArr() {
    local arr=("$@")
    for i in "${arr[@]}"; do
        echo -n "$i "
    done
    echo
}

arr=($@)

printArr "${arr[@]}"
insertionSort arr
printArr "${arr[@]}"
