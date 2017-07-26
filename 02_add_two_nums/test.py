#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from add_two_nums import *

class TestAddTwoSum(unittest.TestCase):
    def test_get_max_len(self):
        l1 = []
        l2 = [1,2]
        result = get_max_len(l1,l2)
        self.assertEqual(result,2)

    def test_get_sum(self):
        arr1 = [1,2,3]
        arr2 = [4,5,6,7,8]
        result = get_sum(arr1,arr2)
        self.assertEqual(result,87975)


if __name__ == '__main__':
    unittest.main()
