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


class Solution3(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        f = [ [ 0 for j in range(m)] for i in range(n) ]
        f[0][0] = grid[0][0]

        for i in range(n):
            if i == 0: continue
            f[i][0] = grid[i][0] + f[i-1][0]
        for j in range(m):
            if j == 0: continue
            f[0][j] = f[0][j-1] + grid[0][j]

        for i in range(n):
            if i == 0: continue
            for j in range(m):
                if j == 0: continue

                f[i][j] = min([ f[i-1][j], f[i][j-1] ]) + grid[i][j]

        return f[n-1][m-1]

class Solution4(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        f = [ [ 0 for j in range(m)] for i in range(n) ]
        pi = [[-1 for j in range(m)] for i in range(n)]
        f[0][0] = grid[0][0]

        for i in range(n):
            if i == 0: continue
            f[i][0] = grid[i][0] + f[i-1][0]
            pi[i][0] = 0

        for j in range(m):
            if j == 0: continue
            f[0][j] = f[0][j-1] + grid[0][j]
            pi[0][j] = 1

        for i in range(n):
            if i == 0: continue
            for j in range(m):
                if j == 0: continue

                if f[i-1][j] < f[i][j-1]:
                    pi[i][j] = 0
                else:
                    pi[i][j] = 1

                f[i][j] = min([ f[i-1][j], f[i][j-1] ]) + grid[i][j]

        length = m + n - 1
        path = []
        i = n - 1
        j = m - 1

        path.append(grid[i][j])
        for k in range(length):
            if k == 0: continue

            if pi[i][j] == 1:
                j -= 1
            else:
                i -= 1
            path.append(grid[i][j])

        print(path[::-1])

        return f[n-1][m-1]

#print path
class Solution4(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        f = [ [ 0 for j in range(m)] for i in range(n) ]
        pi = [[-1 for j in range(m)] for i in range(n)]
        f[0][0] = grid[0][0]

        for i in range(n):
            if i == 0: continue
            f[i][0] = grid[i][0] + f[i-1][0]
            pi[i][0] = 0

        for j in range(m):
            if j == 0: continue
            f[0][j] = f[0][j-1] + grid[0][j]
            pi[0][j] = 1

        for i in range(n):
            if i == 0: continue
            for j in range(m):
                if j == 0: continue

                if f[i-1][j] < f[i][j-1]:
                    pi[i][j] = 0
                else:
                    pi[i][j] = 1

                f[i][j] = min([ f[i-1][j], f[i][j-1] ]) + grid[i][j]

        length = m + n - 1
        path = []
        i = n - 1
        j = m - 1

        path.append(grid[i][j])
        for k in range(length):
            if k == 0: continue

            if pi[i][j] == 1:
                j -= 1
            else:
                i -= 1
            path.append(grid[i][j])

        print(path[::-1])

        return f[n-1][m-1]

#rolling array
class Solution5(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        f = [ [ 0 for j in range(m)] for i in range(2) ]

        new = old = 0
        for i in range(n):
            old = new
            new = 1 - old
            for j in range(m):
                if i == 0 and j == 0:
                    f[new][j] = grid[0][0]
                    continue

                if i == 0:
                    f[new][j] = grid[i][j] + f[new][j-1]
                elif j == 0:
                    f[new][j] = grid[i][j] + f[old][j]
                else:
                    f[new][j] = min([ f[old][j], f[new][j-1] ]) + grid[i][j]

        return f[new][m-1]

#rolling array + print path
class Solution6(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        down = 0
        right = 1

        f = [ [ 0 for j in range(m)] for i in range(2) ]
        pi = [[-1 for j in range(m)] for i in range(n)]

        new = old = 0
        for i in range(n):
            old = new
            new = 1 - old
            for j in range(m):
                if i == 0 and j == 0:
                    f[new][j] = grid[0][0]
                    continue


                if i == 0:
                    f[new][j] = grid[i][j] + f[new][j-1]
                    pi[i][j] = right
                elif j == 0:
                    f[new][j] = grid[i][j] + f[old][j]
                    pi[i][j] = down
                else:

                    if f[old][j] < f[new][j-1]:
                        pi[i][j] = down
                    else:
                        pi[i][j] = right

                    f[new][j] = min([ f[old][j], f[new][j-1] ]) + grid[i][j]

        length = m + n - 1
        x = n - 1
        y = m - 1
        path = []
        path.append(grid[i][j])
        for k in range(length):
            if k == 0: continue
            if pi[x][y] == down:
                x -= 1
            else:
                y -= 1
            path.append(grid[x][y])
        print(path[::-1])

        return f[new][m-1]


if __name__ == '__main__':
    data = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
    ]

    print( Solution6().minPathSum(data) )
    