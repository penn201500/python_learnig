#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from get_longest_sub_string import *


class TestLongestSubString(unittest.TestCase):

    def test_get_longest_sub_string(self):
        test = Solution()
        result = test.get_longest_sub_string("abcabcbb")
        self.assertEqual(result, 3)

        result = test.get_longest_sub_string("bbbbbb")
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
