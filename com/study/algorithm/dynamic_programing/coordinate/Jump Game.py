# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 11:16
# @Author  : piguanghua
# @FileName: Jump Game.py
# @Software: PyCharm

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        f = [False for i in range(n)]
        f[0] = True
        for i in range(1, n):
            for j in range(i):
                if f[j] == True:
                    if nums[j] + j >= i:
                        f[i] = True
                        break

        return f[-1]


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print( Solution().canJump(nums) )