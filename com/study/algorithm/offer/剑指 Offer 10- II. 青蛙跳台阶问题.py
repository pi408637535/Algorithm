class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 1

        f = [1 for i in range(n+ 1)]
        f[1] = 1


        for i in range(2,n + 1):
            f[i] = f[i -1] +f[i-2]

        return f[n] % 1000000007

if __name__ == '__main__':
    n = 7
    print( Solution().numWays(n) )