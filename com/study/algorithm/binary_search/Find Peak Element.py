# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 15:25
# @Author  : piguanghua
# @FileName: Find Peak Element.py
# @Software: PyCharm

import sys

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        start = 0
        end = len(nums) -1
        while start + 1 < end:
            mid = int((start + end) / 2)
            if nums[mid] > nums[mid- 1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid- 1]:
                start = mid
            else:
                end = mid

        #此时 start+1 = end
        if nums[start] > nums[end]: #已经到数组的0索引位置了
            return start
        elif nums[end] > nums[start]:#已经到数组的n-1索引位置了
            return end

        # 此时 start = end
        if nums[start] > nums[start - 1] and nums[start] > nums[start -1]:
            return start


if __name__ == '__main__':
    nums = [2,1,2]
    print( Solution().findPeakElement(nums) )