# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 15:58
# @Author  : piguanghua
# @FileName: Triangle.py
# @Software: PyCharm

import numpy as np

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        m = len(triangle[-1])
        f = [ [0 for j in range(m)] for i in range(n)]

        f[0][0] = triangle[0][0]
        for i in range(1, n):
            f[i][0] += triangle[i][0] + f[i-1][0]

        for i in range(1, n):
            f[i][i] += triangle[i][-1] + f[i - 1][i-1]

        for i in range(2, n):
            for j in range(1, i):
                f[i][j] = min( [ f[i-1][j-1] + triangle[i][j], \
                                 f[i-1][j] + triangle[i][j] ] )
                
        return min(f[-1][:])


        #codition


if __name__ == '__main__':
    triangle = [
        [2],
        [ 3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    print( Solution().minimumTotal(triangle) )
