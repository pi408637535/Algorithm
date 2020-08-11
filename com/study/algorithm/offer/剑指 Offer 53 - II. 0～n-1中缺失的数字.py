# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 17:28
# @Author  : piguanghua
# @FileName: 剑指 Offer 53 - II. 0～n-1中缺失的数字.py
# @Software: PyCharm


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = (1 + len(nums) ) * len(nums) // 2
        for ele in nums:
            sum -= ele
        return sum


if __name__ == '__main__':
    nums = [0,1,2,3,4,5,6,7,9]
    print(Solution().missingNumber(nums))