# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 13:23
# @Author  : piguanghua
# @FileName: Paint_House.py
# @Software: PyCharm

#descripe
"""
    一排N个房子，每个房子3中三种颜色，相邻两个房子不能同色，求最小花费
"""
import sys

class Solution(object):
    def paint(self, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [ [sys.maxsize for j in range(3)] for i in range(n+1) ]

        for i in range(3):
            f[0][i] = 0

        for i in range(n + 1):
            if i == 0: continue

            f[i][0] = min( [f[i-1][1], f[i-1][2] ] )
            f[i][1] = min([f[i - 1][0], f[i - 1][2]])
            f[i][2] = min([f[i - 1][1], f[i - 1][0]])

        return min( [ f[n][0],f[n][1],f[n][2] ] )

if __name__ == '__main__':
    #data = [[0,0],[0,1]]
    #data = [[1]]
    data = 5
    print(Solution().paint( data ))