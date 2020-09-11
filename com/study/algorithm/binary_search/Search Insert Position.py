# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 14:23
# @Author  : piguanghua
# @FileName: Search Insert Position.py
# @Software: PyCharm

class Solution(object):
    def searchInsert(self, nums, target):
        s = 0
        e = len(nums)-1

        while s + 1 < e:
            mid = s + (e - s) // 2
            if nums[mid] <= target:
                s = mid
            else:
                e = mid

        if target < nums[s]:
            return 0
        if target > nums[e]:
            return len(nums)
        else:
            if nums[s] == target:
                return s
            else:
                return s + 1






if __name__ == '__main__':
    nums = [1,3]
    target = 1
    print( Solution().searchInsert(nums, target) )