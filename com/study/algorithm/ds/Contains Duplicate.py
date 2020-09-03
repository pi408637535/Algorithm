# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 11:25
# @Author  : piguanghua
# @FileName: Contains Duplicate.py
# @Software: PyCharm


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data_dict = {}
        for ele in nums:
            if not data_dict.get(ele):
                data_dict[ele] = True
            else:
                return True

        return False