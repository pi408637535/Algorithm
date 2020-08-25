# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 14:21
# @Author  : piguanghua
# @FileName: Find the Duplicate Number.py
# @Software: PyCharm

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        fast = 0
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if nums[slow] == nums[fast]:
                break

        fast = 0
        while True:

            slow = nums[slow]
            fast = nums[fast]
            if fast == slow:
                return fast


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    nums = [3,1,3,4,2]
    print( Solution().findDuplicate(nums) )
