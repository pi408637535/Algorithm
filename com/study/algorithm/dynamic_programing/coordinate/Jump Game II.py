# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 13:35
# @Author  : piguanghua
# @FileName: Jump Game II.py
# @Software: PyCharm

import sys

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        f = [ sys.maxsize for i in range(n) ]
        f[0] = 0

        for i in range(1, n):
            for j in range(i):
                if f[i] > 0:
                    if nums[j] + j >= i:
                        f[i] = min([ f[i], f[j]+1 ])

        return f[-1]



if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print( Solution().jump(nums) )