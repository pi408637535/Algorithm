# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 10:45
# @Author  : piguanghua
# @FileName: Combination Sum.py
# @Software: PyCharm


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        def dfs(s, target, cur):
            if target == 0:
                ans.append(cur.copy())
                return


            for i in range(s, len(candidates)):
                if candidates[i] > target: break

                cur.append(candidates[i])
                dfs(i, target - candidates[i], cur)
                cur.pop()

        #for i in range(len(candidates)+1):
        dfs(0, target, [])

        return ans


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        def dfs(s, target, cur,depth, n):
            if depth == n:
                if target == 0:
                    ans.append(cur.copy())
                    return


            for i in range(s, len(candidates)):
                if candidates[i] > target: break

                cur.append(candidates[i])
                dfs(i, target - candidates[i], cur, depth + 1, n)
                cur.pop()

        for i in range(int(target / candidates[0]) + 1):
            dfs(0, target, [], 0, i)

        return ans

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7

    print( Solution().combinationSum(candidates, target) )