# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 14:47
# @Author  : piguanghua
# @FileName: 剑指 Offer 45. 把数组排成最小的数.py
# @Software: PyCharm

import  sys
import copy
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        ans = []
        visit = [False] * len(nums)

        def dfs(n, cur):
            if len(cur) == n:
                ans.append(copy.deepcopy(cur))
                return

            for i in range(len(nums)):
                if visit[i] == True: continue
                cur.append(nums[i])
                visit[i] = True
                dfs(n, cur)
                visit[i] = False
                cur.pop()

        dfs(len(nums), [])
        min_nums = []
        for ele in ans:
            num = ""
            for i in ele:
                num += str(i)
            min_nums.append(num)

        return str(min(min_nums))

if __name__ == '__main__':
    nums = [10,2]
    nums = [3, 30, 34, 5, 9]
    nums = [999999998,999999997,999999999]
    print( Solution().minNumber(nums) )
