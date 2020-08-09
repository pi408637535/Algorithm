class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((1+n) * n / 2)

if __name__ == '__main__':
    print(  Solution().sumNums(9) )