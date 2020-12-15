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


# 2020/10/31
import heapq
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_heap = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        heapq.heappush(self.min_heap, x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            ele = self.stack.pop(-1)
            if ele == self.min_heap[0]:
                heapq.heappop(self.min_heap)

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.min_heap[0]
        return -1


'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        self.num = 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.stack.append(x)
        if not self.num:
            self.min_stack.append(x)
        else:
            min_num = self.min_stack[-1]
            if x < min_num:
                self.min_stack.append(x)
            else:
                self.min_stack.append(min_num)

        self.num += 1

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

        self.num -= 1


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
'''


'''
class LinkList():
    def __init__(self, val, min_num, next=None):
        self.val = val
        self.min_num = min_num
        self.next = next


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dummy = LinkList(0,0)


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if not self.dummy.next:
            node = LinkList(x, x)
            self.dummy.next = node
        else:
            node = LinkList(x, min(x, self.dummy.next.min_num))
            node.next = self.dummy.next
            self.dummy.next = node

    def pop(self):
        """
        :rtype: None
        """
        if self.dummy.next:
           self.dummy.next = self.dummy.next.next

    def top(self):
        """
        :rtype: int
        """
        return self.dummy.next.val


    def getMin(self):
        """
        :rtype: int
        """
        return self.dummy.next.min_num
'''




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
