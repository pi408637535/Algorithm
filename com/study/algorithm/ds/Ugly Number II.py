import heapq
import numpy as np
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [1]
        p2 = p3 = p5 = 0

        while max(p2, p3, p5) < n:
            p2_num = f[p2] * 2
            p3_num = f[p3] * 3
            p5_num = f[p5] * 5

            min_num = min(p2_num, p3_num, p5_num)
            if p2_num == min_num:
                p2 += 1
            elif p3_num == min_num:
                p3 += 1
            else:
                p5 += 1
            if min_num not in f:
                f.append(min_num)
            #num = min_num

        return f[n-1]

if __name__ == '__main__':
    n = 10
    print(Solution().nthUglyNumber(n))