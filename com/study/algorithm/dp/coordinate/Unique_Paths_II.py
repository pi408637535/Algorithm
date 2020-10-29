# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 10:03
# @Author  : piguanghua
# @FileName: Unique_Paths_II.py
# @Software: PyCharm
import numpy as np

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """


        f = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]

        #init & condition
        for i in range(len(obstacleGrid)):
            f[i][0] = 1
            if obstacleGrid[i][0] == 1: #行阻塞
                f[i][0] = 0
                break


        for j in range(len(obstacleGrid[0])):
            f[0][j] = 1
            if obstacleGrid[0][j] == 1: #行阻塞
                f[0][j] = 0
                break



        for i in range( len(obstacleGrid) ):
            for j in range( len(obstacleGrid[0])  ):

                if i == 0: continue
                if j == 0: continue

                if obstacleGrid[i][j] == 1: #第一次遇到障碍
                    f[i][j] = 0

                elif obstacleGrid[i-1][j] == 1 or obstacleGrid[i][j-1] ==1:
                    f[i][j] = max([f[i - 1][j], f[i][j - 1]])

                else:
                   f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


if __name__ == '__main__':
    #data = [[0,0],[0,1]]
    #data = [[1]]
    data = [[0,0,0],[0,1,0], [0,0,0]]
    print(Solution().uniquePathsWithObstacles( data ))