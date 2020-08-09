class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        c = a ^ b
        n = (a & b) << 1
        return n + c

if __name__ == '__main__':
    a = -10
    b = -20
    print( Solution().add(a, b) )