# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:31
# @Author  : piguanghua
# @FileName: Triangle.py
# @Software: PyCharm
import sys

class Solution(object):

    def __init__(self):
        self.best = sys.maxsize

    def dfs(self, data, x, y, sum):
        n = len(data)

        if x == n:
            self.best = min([sum, self.best])
            return

        self.dfs(data, x+1, y, sum + data[x][y])
        self.dfs(data, x + 1, y+1, sum + data[x][y])

    def find(self, data):
        '''
        dfs:
            用途:移动到下一行相邻数字上  : 两种操作[i+1][j],[i+1][j+1]
            数据规模:顶层->底层，数据规模变小 :
            terminal condition:最底层+1 :比较min
        '''
        self.dfs(data, 0, 0, 0)
        return self.best

class Solution2(object):


    #devide-conquer
    #与递归最大不同:没有利用全局变量
    #devide后，每层可走步骤都要最小
    '''
           [2]
          min
        [3]  [4]
         min
      [5]  [6]  [7]
    '''
    def helper(self, data, x, y):
        n = len(data)

        if x == n:
            return 0
        else:
            return data[x][y] + min([ self.helper(data, x+1, y),
                                      self.helper(data, x + 1, y+1)])


    def find(self, data):


        return self.helper(data, 0, 0)

#动态规划，记忆化搜索
class Solution3(object):

    def __init__(self, n ):
        hash = [[sys.maxsize for i in range(n)] for j in range(n)]
        self.hash = hash

    #devide-conquer
    #与递归最大不同:没有利用全局变量
    #devide后，每层可走步骤都要最小
    '''
           [2]
          min
        [3]  [4]
         min
      [5]  [6]  [7]
    '''
    def helper(self, data, x, y):
        n = len(data)

        if n == x:
            return 0

        #get min path for (x,y) to bottom
        if self.hash[x][y] != sys.maxsize:
            return self.hash[x][y]

        #set before return
        self.hash[x][y] = data[x][y] + min([ self.helper(data, x+1, y),
                                      self.helper(data, x + 1, y+1)])

        return self.hash[x][y]


    def find(self, data):
        return self.helper(data, 0, 0)


if __name__ == '__main__':
    #求数字三角形的最小值
    #要求:每一步仅能移动到下面的一行的相邻数字上
    data = [
        [2],
        [3,4],
        [5,6,7],
        [4,0,1,3]
    ]

    print( Solution3(4).find(data) )
