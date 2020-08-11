# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 15:38
# @Author  : piguanghua
# @FileName: 剑指 Offer 48. 最长不含重复字符的子字符串.py
# @Software: PyCharm

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        length = len(s)

        for i in range(length):
            visit = {}
            j = i
            while j < length and not visit.get(s[j],False):
                visit[s[j]] = True
                j += 1
            ans = max(j - i, ans)


        return ans



if __name__ == '__main__':
    s = "abcabcbb"
    s = "bbbbbb"
    s = "pwwkew"
    s = "dvdf"
    print( Solution().lengthOfLongestSubstring(s) )