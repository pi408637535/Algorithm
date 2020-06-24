# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 09:22
# @Author  : piguanghua
# @FileName: Unique_Paths.py
# @Software: PyCharm
import numpy as np

class Solution(object):
    def uniquePaths(self, column, row):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [ [ 0 for i in range(column) ] for j in range(row) ]

        for i in range(column):
            f[0][i] = 1

        for j in range(row):
            f[j][0] = 1
        
        
        for i in range(row):
            for j in range(column):
                
                if i == 0: continue
                if j == 0: continue
                
                f[i][j] = f[i-1][j] + f[i][j-1]
 

        return f[row-1][column-1]
    


if __name__ == '__main__':
    print( Solution().uniquePaths(3,2) )