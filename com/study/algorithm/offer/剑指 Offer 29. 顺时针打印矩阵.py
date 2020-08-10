# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 12:05
# @Author  : piguanghua
# @FileName: 剑指 Offer 29. 顺时针打印矩阵.py
# @Software: PyCharm

#重点， 方向数组:[[0,1],[1,0],[0,-1],[-1,0]]
# direction 转向条件 5个：next_row < 0 or next_row >= m or next_column < 0 or next_column >=n or visit[next_row][next_column] ==True:
# row,column下一个方向: 通过direction和方向数组 来确定

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)

        if m == 0:
            return []

        n = len(matrix[0])

        if n == 0:
            return []

        total = m * n
        direction = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        row = 0
        column = 0
        data = []
        visit = [ [False for j in range(n)] for i in range(m) ]
        for i in range(total):
            data.append(matrix[row][column])
            visit[row][column] = True
            next_row = row + directions[direction][0]
            next_column = column + directions[direction][1]

            if next_row < 0 or next_row >= m or next_column < 0 or next_column >=n or visit[next_row][next_column] ==True:
                direction = (direction + 1) % 4

            row += directions[direction][0]
            column += directions[direction][1]

        return data




if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print( Solution().spiralOrder(matrix) )
