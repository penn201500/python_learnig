#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def split_array(self, target):
        arr = []
        left = 0
        i = 0
        while i < (len(target)-1):
            print(i)
            if (i+1 == len(target)-1):
                arr.append(target[left+1 : len(target)])
                break
            elif target[i + 1] in target[left : i+1]:
                print(target[i+1])
                print(target[left:i+1])
                arr.append(target[left : i+1])
                left = i + 1
                i += 1
            else:
                i += 1
        return arr

    def get_longest_sub_string(self, target):
        arr = self.split_array(target)
        max_sub_string = max(arr, key = lambda x: len(x))
        return len(max_sub_string)


if __name__ == '__main__':
    target = "ababcs"
    test = Solution()
    arr = test.split_array(target)
    print(arr)
    print(test.get_longest_sub_string(arr))
