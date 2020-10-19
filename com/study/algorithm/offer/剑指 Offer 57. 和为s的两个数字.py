# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 12:16
# @Author  : piguanghua
# @FileName: 剑指 Offer 57. 和为s的两个数字.py
# @Software: PyCharm

import copy
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1


        while i != j:
            if nums[j] > target:
                j -= 1
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
            elif nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
        return []


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]

            dic[nums[i]] = i

        return []


if __name__ == '__main__':
    nums = [5, 2, 6]
    target = 8
    nums = [2, 7, 11, 15]
    target = 9

    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))

if __name__ == '__main__':
    #nums = [10,18,25,33,36,50,50,52,57,74]
    #target = 126
    nums = [2,7,11,15]
    target = 9
    print( Solution().twoSum(nums, target) )