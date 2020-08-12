# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 14:28
# @Author  : piguanghua
# @FileName: Two Sum.py
# @Software: PyCharm


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index,ele in enumerate(nums):
            dic[ele] = index

        for ele in nums:
            if dic.get(target - ele):
                return [dic[ele], dic.get(target - ele)]


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
            if nums[j] > target:
                j -= 1
            if nums[i] + nums[j] == target:
                return [i,j]
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
        falg = False
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if not falg:
                    if nums[i] + nums[j] == target:
                        falg = True
                        res = [i,j]
        return res

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    print( Solution().twoSum(nums, target) )