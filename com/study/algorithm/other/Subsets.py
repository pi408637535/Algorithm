# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 09:36
# @Author  : piguanghua
# @FileName: Subsets.py
# @Software: PyCharm

import copy

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(n, s, cur):
            if len(cur) == n:

                ans.append(copy.deepcopy(cur))
                return

            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs(n, i+1, cur)
                cur.pop()

        for i in range(len(nums)+1):
            dfs(i, 0, [])

        return ans

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)

        return [ [nums[i] for i in range(n) if s & 1 << i >> 0]  for s in range(1 << n)]


if __name__ == '__main__':
    nums = [1,2,3]
    print( Solution().subsets(nums) )