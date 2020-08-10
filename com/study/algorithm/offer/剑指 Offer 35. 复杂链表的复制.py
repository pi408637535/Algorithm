# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 17:00
# @Author  : piguanghua
# @FileName: 剑指 Offer 35. 复杂链表的复制.py
# @Software: PyCharm


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic = {}
        dummy = Node(0)
        pre = dummy

        while head != None:
            if not dic.get(head):
                dic[head] = Node(head.val)


            if head.random :
                if not dic.get(head.random):
                    dic[head.random] = Node(head.random.val)
                    dic[head].random = dic[head.random]
                else:
                    dic[head].random = dic[head.random]

            pre.next = dic[head]
            pre = pre.next
            head = head.next

        return dummy.next

if __name__ == '__main__':
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)


    Node1.next = Node2
    Node2.next = Node3

    Node2.random = Node1

    print(Solution().copyRandomList(Node1))


