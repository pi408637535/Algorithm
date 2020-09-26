# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 15:12
# @Author  : piguanghua
# @FileName: 剑指 Offer 47. 礼物的最大价值.py
# @Software: PyCharm

import numpy as np

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        f = [ [0 for j in range(n)]for i in range(m)]

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    f[i][j] = grid[i][j]
                elif i == 0:
                    f[i][j] = f[i][j-1] + grid[i][j]
                elif j == 0:
                    f[i][j] = f[i - 1][j] + grid[i][j]
                else:
                    f[i][j] = max([f[i-1][j], f[i][j-1]]) + grid[i][j]

        return f[m-1][n-1]

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        f = [[0] * n  for i in range(m)]

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    f[i][j] = grid[i][j]

                elif i == 0 and j != 0:
                    f[i][j] = grid[i][j] + f[i][j-1]
                elif j == 0 and i != 0:
                    f[i][j] = grid[i][j] + f[i-1][j]
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1]) + grid[i][j]

        return f[i][j]


if __name__ == '__main__':
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
    ]
    print(Solution().maxValue(grid))