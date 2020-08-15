# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 17:38
# @Author  : piguanghua
# @FileName: 剑指 Offer 49. 丑数.py
# @Software: PyCharm

import heapq
import collections
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        visit = {}
        heap = []

        if n == 1:
            return 1

        #queue = collections.deque([1,2,3,5])
        basic = [2,3,5]
        for ele in basic:
            heapq.heappush(heap, ele)
            visit[ele] = True


        for i in range(1,n):
            top = heapq.heappop(heap)

            for j in range(3):
                num = top * basic[j]
                if not visit.get(num, False):
                    visit[num] = True
                    #queue.append(num)
                    heapq.heappush(heap, num)
            #top = heapq.heappop(heap)
        return top



if __name__ == '__main__':
    n = 2
    print( Solution().nthUglyNumber(n) )
