# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 17:38
# @Author  : piguanghua
# @FileName: 剑指 Offer 49. 丑数.py
# @Software: PyCharm

import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        visit = {}
        heap = []
        heapq.heappush(heap, 1)
        heapq.heappush(heap, 2)
        heapq.heappush(heap, 3)
        heapq.heappush(heap, 5)

        ans = []
        ans.append(1)
        
        for i in range(n):
            top = heapq.heappop(heap)

            for j in range(len(heap)):
                num = top * heap[j]
                if not visit.get(num, False):
                    visit[num] = True
                    ans.append(num)
                    heapq.heappush(heap, num)

        return ans[n]



if __name__ == '__main__':
    n = 12
    print( Solution().nthUglyNumber(n) )
