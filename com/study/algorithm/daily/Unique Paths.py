import numpy as np

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m and not n:
            return 1

        f = [ [ 0 for j in range(n) ] for i in range(m) ]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    f[i][j] = 1
                elif j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i-1][j] + f[i][j - 1]

        return f[m-1][n-1]

if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7) )