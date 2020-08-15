# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 17:40
# @Author  : piguanghua
# @FileName: 剑指 Offer 61. 扑克牌中的顺子.py
# @Software: PyCharm

class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f = [True for i in range(len(nums))]
        for i in range(1, 5):
            f[i] = f[i-1] and ( (nums[i] == 0) or (True if nums[i]>nums[i-1] else False))

        positive = f[-1]
        f = [True for i in range(len(nums))]

        for i in range(3, -1, -1 ):
            f[i] = f[i+1] and ( (nums[i] == 0) or (True if nums[i]>nums[i+1] else False))
        negative = f[0]

        return positive or negative


class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1
                continue
            if nums[i] == nums[i+1]:
                return False



        return True if nums[-1] - nums[joker] < 5 else False

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    nums = [0,0,8,5,4]
    #nums = [1,2,12,0,3]
    nums = [13,13,9,12,10]

    print( Solution().isStraight(nums) )