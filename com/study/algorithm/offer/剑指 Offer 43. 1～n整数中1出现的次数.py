# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 13:56
# @Author  : piguanghua
# @FileName: 剑指 Offer 43. 1～n整数中1出现的次数.py
# @Software: PyCharm

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0

        for i in range(1, n+1):

            while i != 0:
                if i < 10: sum += 1 if i == 1 else 0
                else:
                    sum += 1 if i % 10 == 1 else 0
                i = i // 10

        return sum


if __name__ == '__main__':
    n = 13
    print( Solution().countDigitOne(n) )