# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 16:16
# @Author  : piguanghua
# @FileName: Ugly Nuber.py
# @Software: PyCharm

import heapq

class Solution(object):
    def isUgly(self, num):

        if num == 1:
            return True

        q = []
        inQ = {}

        primes = [2,3,5]

        for i in range(3):
            heapq.heappush(q, primes[i])
            inQ[primes[i]] = True


        i = 0
        while i < num:
            number = heapq.heappop(q)
            for j in range(3):
                if number * primes[j] not in inQ.keys():
                    heapq.heappush(q, number * primes[j])
                    inQ[number * primes[j]] = True
            i += 1

        return inQ.get(num, False)


class Solution(object):
    def isUgly(self, num):
        if num == 1:
            return True

        arrays = [2,3,5]

        flag = False
        while num > 0:
            for i in range(3):
                if num % arrays[i] == 0:
                    flag = True
                    break

            if flag == True:
                num = num / arrays[i]
                flag = False
            else:
                break

        if num != 1:
            return False
        else:
            return True





if __name__ == '__main__':
    print( Solution().isUgly(214797179) )
