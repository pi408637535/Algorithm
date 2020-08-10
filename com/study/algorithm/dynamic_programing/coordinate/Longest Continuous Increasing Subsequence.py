# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 09:43
# @Author  : piguanghua
# @FileName: Longest Continuous Increasing Subsequence.py
# @Software: PyCharm


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 0:
            return 0

        f = [1 for i in range(length)]

        for i in range(1, length):
            if nums[i] - nums[i-1] > 0:
                f[i] = f[i-1] + 1

        return max(f)

if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]

    nums = [2,1]
    nums = [1,3,5,4,7]

    print( Solution().findLengthOfLCIS(nums) )