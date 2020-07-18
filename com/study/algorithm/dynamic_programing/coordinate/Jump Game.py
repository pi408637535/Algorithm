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


class Solution1(object):
    def canJump(self, nums):
        n = len(nums)

        if n == 1:
            return True

        #f = [False for i in range(n)]

        #f[0] = True
        i = 0
        j = 0
        while i < n:
            j = nums[j] + j
            if j >= n-1:
                break
            else:
                i+=1
        if j >= n:
            return True
        else:
            return False


if __name__ == '__main__':
    #nums = [2,3,1,1,4]
    #nums = [3,2,1,0,4]
    #nums = [2,0]
    #nums = [2, 0, 0]
    nums = [2,3,1,1,4]

    print( Solution1().canJump(nums) )