import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [ sys.maxsize for i in range(n + 1)]
        f[0] = 0
        for i in range(n + 1):

            j = 1
            while j * j <= n:
                f[i] = min(f[i - j*j]+1, f[i]  )
                j+=1

        return f[i]



if __name__ == '__main__':
    input = 6554
    print( Solution().numSquares(input) )