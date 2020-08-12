# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 14:56
# @Author  : piguanghua
# @FileName: Two Sum II - Input array is sorted.py
# @Software: PyCharm

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1

        nums.sort()

        while  i != j:
            #if nums[j] > target:
                #j -= 1
            if nums[i] + nums[j] == target:
                return [i+1,j+1]
            elif nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
        return []

if __name__ == '__main__':
    numbers = [-1,0]
    target = -1

    print(Solution().twoSum(numbers, target))
