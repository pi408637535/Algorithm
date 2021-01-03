import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        f = [ [0 for j in range(5)] for i in range(n + 1)]

        f[0][0] = 0
        f[0][1] = -sys.maxsize
        f[0][2] = -sys.maxsize
        f[0][3] = -sys.maxsize
        f[0][4] = -sys.maxsize

        for i in range(1, n + 1):

            for j in [0,2,4]:
                f[i][j] = f[i-1][j]
                if j > 0 and i >=2 and f[i-1][j-1] != -sys.maxsize:
                    f[i][j] = max(f[i-1][j], f[i-1][j-1] + prices[i-1] - prices[i-2] )

            for j in [1,3]:
                f[i][j] = f[i-1][j-1]
                if i >= 2 and f[i-1][j] != -sys.maxsize:
                    f[i][j] = max(f[i-1][j] +prices[i-1] - prices[i-2], f[i-1][j-1])



        return max(f[n][0], f[n][2], f[n][4])


