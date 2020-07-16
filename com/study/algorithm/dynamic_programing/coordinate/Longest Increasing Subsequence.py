# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 15:28
# @Author  : piguanghua
# @FileName: Longest Increasing Subsequence.py
# @Software: PyCharm

import  numpy as np

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n == 0:
            return 0

        f = [1 for i in range(n)]
        #f[0] = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max([ f[i], f[j] + 1 ])

        return max(f)





if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    print( Solution().lengthOfLIS(nums) )