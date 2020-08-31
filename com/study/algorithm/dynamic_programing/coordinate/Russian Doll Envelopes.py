# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 14:57
# @Author  : piguanghua
# @FileName: Russian Doll Envelopes.py
# @Software: PyCharm

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        nums = len(envelopes)
        envelopes = sorted(envelopes, key= lambda ele: ele[0], reverse=True)

        f = [1 for i in range(nums)]

        for i in range(nums):
            if i == 0: continue
            for j in range(i):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    f[i] = max(1, f[j] + 1, f[i])

        return max( f )
    
        
if __name__ == '__main__':
    input = [[1,2],[2,3],[3,4],[1,2]]
    print( Solution().maxEnvelopes(input) )