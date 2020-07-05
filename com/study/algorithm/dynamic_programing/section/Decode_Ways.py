# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 14:25
# @Author  : piguanghua
# @FileName: Decode_Ways.py
# @Software: PyCharm

#Given a non-empty string containing only digits

class Solution(object):


    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1:
            if s[0] == "0": return 0

        two_char_list = [ str(i+11) for i in range(16)]
        one_char_list = [ str(i+1) for i in range(26)]

        f = [0 for i in range(len(s) + 1) ]
        f[0] = 0

        for i in range(len(s) + 1):
            if i < 1: continue


            if s[i-1] in one_char_list:
                f[i] = f[i - 1]


            if i >=2 and str(s[i-2]+s[i-1]) in two_char_list:
                f[i] += f[i-2]


        return f[-1]


if __name__ == '__main__':
    #data = "226"
    #data = "12"   #2
    data = "10" #1
    #data = "00" #0
    print( Solution().numDecodings(data)  )