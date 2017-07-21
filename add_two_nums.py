#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_max_len(arr1,arr2):
    if len(arr1) >= len(arr2):
        return len(arr1)
    else:
        return len(arr2)


def get_sum(arr1,arr2):
    len_arr3 = get_max_len(arr1,arr2)
    arr3 = [0]*len_arr3
    print("init",arr3)

    for i in range(len_arr3):
        if arr1[1]+arr2[i] >=10:
            arr3[i] += arr1[i]+arr2[i]-10
            arr3[i+1] = 1
        else:
            arr3[i] += arr1[i]+arr2[i]
    print(arr3)


if __name__ == '__main__':
    arr1 = [1,2,3]
    arr2 = [4,5,6]
    get_sum(arr1,arr2)
