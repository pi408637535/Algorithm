# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 11:22
# @Author  : piguanghua
# @FileName: 剑指 Offer 16. 数值的整数次方.py
# @Software: PyCharm

#二分法
#需要注意点: n % 2 == 0 为奇数时 左 * 右 * x
                    #偶数是 左 * 右

class Solution(object):

    def helper(self,x , n):
        if n == 0:
            return 1
        if n == 1:
            return x


        if n & 1:
            return self.helper(x * x, n // 2) * x
        return self.helper(x * x, n // 2)

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = 1 if n > 0 else -1
        n = n * flag

        result = self.helper(x, n)

        if flag > 0:
            return result
        else:
            return 1 / result




if __name__ == '__main__':
    x = 0.1
    n = 214

    print( Solution().myPow(x, n) )