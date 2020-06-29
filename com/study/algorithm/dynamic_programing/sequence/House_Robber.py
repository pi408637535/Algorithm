# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 16:39
# @Author  : piguanghua
# @FileName: House_Robber.py

'''
思路:https://www.jianshu.com/p/2ebb90c4e329
'''
import numpy as np


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 0:
            return 0

        f = [ [0 for j in range(2)] for i in range(n + 1) ]

        for i in range(n+1):
            if i == 0: continue

            f[i][0] = max( [f[i-1][0], f[i-1][1] ] )

            f[i][1] = nums[i-1] + f[i-1][0]
        
        return max( [ f[i][0], f[i][1] ]  )

if __name__ == '__main__':
    nums = [1]
    print( Solution().rob(nums)  )