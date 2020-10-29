class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0 for i in range(n+1)]
        f[0] = 1
        f[1] = 1

        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]

        return f[n]

# 2020.10.28
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * (n+1)
        f[0] = 1
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i - 2]

        return f[n]


if __name__ == '__main__':
    n = 4
    print(Solution().climbStairs(n))