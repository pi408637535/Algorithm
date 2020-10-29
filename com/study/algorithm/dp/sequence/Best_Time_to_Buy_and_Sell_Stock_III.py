# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 11:04
# @Author  : piguanghua
# @FileName: Best Time to Buy and Sell Stock III.py
# @Software: PyCharm

import sys
import numpy as np

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        f = [ [0 for j in range(6)] for i in range(n + 1) ]

        for i in range(6):
            if i == 0: continue
            f[0][i] = -sys.maxsize

        for i in range(n):
            if i == 0: continue

            for j in range(6):
                if j == 0: continue

                if j % 2 == 0:
                    f[i][j] = max([ f[i-1][j] + prices[i] - prices[i - 1], f[i-1][j-1] ])
                else:
                    f[i][j] = max([f[i - 1][j], f[i - 1][0] + prices[i] - prices[i - 1]])

        return max( f[i][1], f[i][3],f[i][5],  )


if __name__ == '__main__':
    data = [3,3,5,0,0,3,1,4]
    print( Solution().maxProfit(data) )