# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 11:22
# @Author  : piguanghua
# @FileName: 剑指 Offer 38. 字符串的排列.py
# @Software: PyCharm


class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        used = [False] * len(s)

        def dfs(n, cur):

            if n == len(cur):
                if "".join(cur) not in ans:
                    ans.append("".join(cur.copy()))
                return

            for i in range(len(s)):
                if used[i] == True: continue
                cur.append(s[i])
                used[i] = True
                dfs(n, cur)
                cur.pop()
                used[i] = False

        dfs(len(s), [])
        ans = ["".join(ele) for ele in ans]
        return ans



if __name__ == '__main__':
    s = "zg"
    print( Solution().permutation(s) )