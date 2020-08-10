# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 13:30
# @Author  : piguanghua
# @FileName: 剑指 Offer 30. 包含min函数的栈.py
# @Software: PyCharm

#调用 min、push 及 pop 的时间复杂度都是 O(1)，所以需要建立两个 数据栈stackA,辅助栈stackB
# 数据栈stackA 维持正常的 push,pop
# stackB, 维持min,降序

import heapq
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackA = []
        self.stackB = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stackA.append(x)
        heapq.heappush(self.stackB, x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stackA) == 0:
            return None
        else:
            item = self.stackA.pop()
            if item == self.stackB[0]:
                heapq.heappop(self.stackB)

            return item



    def top(self):
        """
        :rtype: int
        """
        return self.stackA[-1]


    def min(self):
        """
        :rtype: int
        """
        return self.stackB[0]

if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)

    print(obj.min())
    print(obj.pop())
    print(obj.top())
    print(obj.min())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
