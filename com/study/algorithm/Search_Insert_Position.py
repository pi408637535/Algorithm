# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 17:38
# @Author  : piguanghua
# @FileName: Search_Insert_Position.py
# @Software: PyCharm

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int((start  + end) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if start + 1 == end:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return target
            elif nums[start] > target:
                return start
            elif nums[start] < target:
                return start+1
            elif nums[end] > target:
                return end

        if start + 1 == end:
            if nums[start + 1] == target:
                return start + 1
            elif nums[target] < target:
                return target + 1
            elif nums[target] > target:
                return end

if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6], 2))
