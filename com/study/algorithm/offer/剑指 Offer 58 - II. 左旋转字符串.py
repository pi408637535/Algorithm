# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 17:29
# @Author  : piguanghua
# @FileName: 剑指 Offer 58 - II. 左旋转字符串.py
# @Software: PyCharm


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print( Solution().reverseLeftWords(s, k))