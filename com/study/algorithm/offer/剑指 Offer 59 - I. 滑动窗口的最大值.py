# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 17:18
# @Author  : piguanghua
# @FileName: 剑指 Offer 59 - I. 滑动窗口的最大值.py
# @Software: PyCharm

import sys
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        ans = []
        for i in range(len(nums) - k + 1):
            ans.append(max(nums[i:k+i]))

        return ans

if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print( Solution().maxSlidingWindow(nums, k) )