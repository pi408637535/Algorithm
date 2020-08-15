class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        ans = 0
        for i in range(2, n+1):
            ans = (ans + m) % i
            print(ans)
        return ans

if __name__ == '__main__':
    n = 5
    m = 3
    print( Solution().lastRemaining(n, m) )