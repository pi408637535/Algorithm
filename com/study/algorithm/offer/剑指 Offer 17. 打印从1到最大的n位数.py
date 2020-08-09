
import math

class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        max_num = int(math.pow(10, n))
        data = [ i for i in range(max_num)]
        return data[1:]


if __name__ == '__main__':
    n = 1
    print( Solution().printNumbers(n) )