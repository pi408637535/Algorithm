# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 13:58
# @Author  : piguanghua
# @FileName: 剑指 Offer 31. 栈的压入、弹出序列.py
# @Software: PyCharm

#思路:一边stack压，一边比对弹出顺序，如果值一样就stack弹出并且弹出序列向后一位
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0

        for ele in pushed:
            stack.append(ele)

            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return False if stack else True


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]

    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]

    print( Solution().validateStackSequences(pushed, popped) )