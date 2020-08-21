# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 17:23
# @Author  : piguanghua
# @FileName: House Robber II.py
# @Software: PyCharm

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        f = [[0 for j in range(2)]for i in range(n)]
        f[0][0] = 0
        f[0][1] = nums[0]

        for i in range(1, n - 1):
            f[i][0] = max([f[i-1][0], f[i-1][1]])
            f[i][1] = f[i-1][0] + nums[i]

        max_num = max(f[n - 2])


        f[1][0] = 0
        f[1][1] = nums[1]
        for i in range(2, n):
            f[i][0] = max([f[i - 1][0], f[i - 1][1]])
            f[i][1] = f[i - 1][0] + nums[i]

        return max( [max(f[-1]),max_num])




if __name__ == '__main__':
    nums = [2,3,2]
    nums = [1,2,3,1]
    nums = [1, 2]

    print(Solution().rob(nums))