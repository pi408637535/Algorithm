# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 13:27
# @Author  : piguanghua
# @FileName: Move Zeroes.py
# @Software: PyCharm


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)


        if n == 0:
            return []


        i = 0
        j = i
        while j < n:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        j = n - 1
        while j >  i - 1:
            nums[j] = 0
            j -= 1

        return nums



if __name__ == '__main__':
    nums = [2,1]
    nums = [0,1,0,3,12]
    print( Solution().moveZeroes(nums) )