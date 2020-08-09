class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        f = [0 for i in range(n+1)]
        f[1] = 1

        for i in range(2,n+1):
            f[i] = f[i-1] + f[i - 2]

        return f[n] % 1000000008



if __name__ == '__main__':
    n = 45
    print( Solution().fib(n) )
