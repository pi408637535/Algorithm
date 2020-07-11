# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 15:54
# @Author  : piguanghua
# @FileName: Search in Rotated Sorted Array.py
# @Software: PyCharm

class Solution:

    def binary_serarh(self, nums, target):

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = int((start + end)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1

    def search(self, nums, target):

        if len(nums) == 0:
            return -1

        if nums[0] < nums[-1]:
            return self.binary_serarh(nums, target)

        start = 0
        end = len(nums) -1

        while start + 1 < end:
            mid = int( (start + end) / 2)
            if nums[mid] == target:
                return mid
            elif target <= nums[mid] and target > nums[end] or \
                    target == nums[mid-1] :
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1


if __name__ == '__main__':
    #nums = [4, 5, 6, 7, 0, 1, 2]
    #target = 1

    #nums = [1,3,5]
    #target = 5

    #nums = [5,1,3]
    #target = 5

    #nums = [4,5,6,7,0,1,2]
    #target = 5

    #nums = [4, 5, 6, 7, 8, 1, 2, 3]
    #target =8

    #nums = [1, 2, 3, 4, 5, 6]
    #target = 1

    nums = [6,7,1,2,3,4,5]
    target = 6

    print( Solution().search(nums, target) )
