class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) +self.fib(n - 2)

if __name__ == '__main__':
    print( Solution().fib(3) )