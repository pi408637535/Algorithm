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
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[start] < target and nums[end] >= target:
                return end
        elif nums[start] > target:
            return start


        if start + 1 == end or start == end:
            if nums[start] == target:
                return start
            elif nums[end] < target:
                return end+1
            else:
                return start



if __name__ == '__main__':
    print(Solution().searchInsert([1], 1))
