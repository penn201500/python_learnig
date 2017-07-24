#!/usr/bin/env python3
# -*- coding: utf-8 -*-

arr = [1,2,3,4,5]
for i in range(len(arr)):
    if 6-arr[i] in arr[i+1:]:
        print(i,arr[i])
        print(arr.index(6-arr[i]),(6-arr[i]))
