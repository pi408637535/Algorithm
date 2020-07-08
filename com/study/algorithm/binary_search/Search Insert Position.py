# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 14:23
# @Author  : piguanghua
# @FileName: Search Insert Position.py
# @Software: PyCharm

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1

        while start+1 < end:
            mid = int((start + end)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] >= target:
            return 0
        if nums[end] >= target:
            return end
        else:
            return end+1






if __name__ == '__main__':
    nums = [1,3]
    target = 1
    print( Solution().searchInsert(nums, target) )