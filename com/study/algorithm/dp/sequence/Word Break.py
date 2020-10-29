# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 09:53
# @Author  : piguanghua
# @FileName: Word Break.py
# @Software: PyCharm

import numpy as np

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        f = [True] + n * [False]

        #f[0][0] = True if s[0] in wordDict else False
        #pre = 0 贪心
        for i in range(n):
            if f[i+1] == False:

                for word in wordDict:
                    if len(word) <= len(s[i:]):
                        if s[i:i+len(word)] == word:
                            f[i+len(word)] = True

        return f[-1]



if __name__ == '__main__':
    #s = "leetcode"
    #wordDict = ["leet", "code"]

    #s = "applepenapple"
    #wordDict = ["apple", "pen"]

    #s = "catsandog"
    #wordDict = ["cats", "dog", "sand", "and", "cat"]

    s = "aaaaaaa"
    wordDict=["aaaa","aaa"]

    print( Solution().wordBreak(s, wordDict) )


