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
import numpy as np

class Solution(object):
    def paint(self, data):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        n = len(data)
        c = len(data[0])
        f = [ [0 for j in range(c)] for i in range(n+1) ]

        #时间复杂度 n * C * C
        for i in range(n + 1):
            if i == 0: continue
            for j in range(c):
                f[i][j] = data[i-1][j]
                previous_cos = []
                for k in range(c):
                   if k != j:
                       previous_cos.append( f[i-1][k] )

                f[i][j] += min( previous_cos )

        min_cos = []
        for i in range(c):
            min_cos.append(f[n][i])

        return min( min_cos )


class Solution2(object):
    def paint(self, data):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        n = len(data)
        c = len(data[0])
        f = [ [0 for j in range(c)] for i in range(n+1) ]
        id1 = id2 = 0

        #时间复杂度 n * C * 2
        for i in range(n + 1):
            if i == 0: continue

            #find min1,min2 #Todo 优化点
            min1 = min2 = sys.maxsize
            for j in range(c):
                if f[i-1][j] < min1:
                    min2 = min1
                    id2 = id1
                    min1 = f[i-1][j]
                    id1 = j
                elif f[i-1][j] < min2:
                    min2 = f[i-1][j]
                    id2 = j

            for j in range(c):
                f[i][j] = data[i-1][j]
                if j != id1:
                    f[i][j] += min1
                else:
                    f[i][j] += min2

        min_cos = []
        for i in range(c):
            min_cos.append(f[n][i])

        return min( min_cos )


if __name__ == '__main__':
    #data = [[0,0],[0,1]]
    #data = [[1]]
    data = [[14,2,11],[11,14,5],[14,3,10]]
    print(Solution2().paint( data ))