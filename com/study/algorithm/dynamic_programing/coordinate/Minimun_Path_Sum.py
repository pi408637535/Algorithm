import numpy as np
import sys

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        f = [ [0 for j in range(len(grid[0])  )]  for i in range( len(grid) ) ]

        f[0][0] = grid[0][0]
        for i in range( len(grid) ):
            if i != 0:
                f[i][0] = f[i-1][0] + grid[i][0]

        for j in range(len(grid[0])):
            if j != 0:
                f[0][j] = f[0][j - 1] + grid[0][j]
        
        for i in range( len(grid)  ):
            for j in range( len(grid[0]) ):
                if i == 0: continue
                if j == 0: continue

                f[i][j] = min( [ f[i-1][j], f[i][j-1]  ]) + grid[i][j]

        return f[len(grid) - 1][ len(grid[0]) - 1 ]

#scolling array
class Solution2(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        f = [[0 for j in range(len(grid[0]) )] for i in range(2)]

        f[0][0] = grid[0][0]
        now,old = 0,0

        for i in range(len(grid)):

            old = now
            now = 1 - now

            for j in range(len(grid[0])):
                if i == 0 and  j == 0 :
                    f[now][j] = grid[i][j]
                    continue

                t = sys.maxsize
                if i > 0:
                    t = min( [t, f[old][j] ] )
                if j > 0:
                    t = min( [t, f[now][j - 1] ] )


                f[now][j] = t + grid[i][j]



        return f[now][len(grid[0]) - 1]


if __name__ == '__main__':
    data = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
    ]

    print( Solution2().minPathSum(data) )
    