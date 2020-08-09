
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n > 0:
            num += n & 1
            n = n >> 1
        return num

if __name__ == '__main__':
    print( Solution().hammingWeight(9) )