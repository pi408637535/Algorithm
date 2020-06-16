# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 09:44
# @Author  : piguanghua
# @FileName: Fibonacci_Number.py
# @Software: PyCharm

#用途：递归计算，接受一个数返回一个数
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        #terminal
        if N == 0:
            return 0
        
        elif N == 1:
            return 1
        
        else:
            #数据规模减少：N-1,N-2
            return self.fib(N - 1) + self.fib(N - 2)


if __name__ == '__main__':
    print(Solution().fib(4) )