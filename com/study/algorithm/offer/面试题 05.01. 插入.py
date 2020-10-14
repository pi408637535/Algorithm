class Solution(object):
    def insertBits(self, N, M, i, j):
        """
        :type N: int
        :type M: int
        :type i: int
        :type j: int
        :rtype: int
        """

        t = 0
        for k in range(j - i + 1):
            t = t | (1 << k + i)
        t = ~t
        N = t & N
        N = N | (M << i)

        return N



if __name__ == '__main__':
    a = 0 & 0
    print(a)
    N = 1024
    M = 19
    i,j = 2,6

    # N = 0
    # M = 31
    # i, j = 0, 4

    print(Solution().insertBits(N, M, i, j))
