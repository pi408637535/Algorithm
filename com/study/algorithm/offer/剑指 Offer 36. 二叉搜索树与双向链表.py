# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 17:29
# @Author  : piguanghua
# @FileName: 剑指 Offer 36. 二叉搜索树与双向链表.py
# @Software: PyCharm


# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#BTS中序遍历是个上升序列
#题目要求：转换成一个排序的循环双向链表。所以要中序遍历
#遍历时 right指代 next,left指代pre

class Solution(object):
    def treeToDoublyList(self, cur):
        """
        :type root: Node
        :rtype: Node
        """

        if cur == None:
            return None

        self.pre = None
        self.head = None

        def dfs(cur):
            if not cur: return
            dfs(cur.left)

            if self.pre:
                self.pre.right = cur
                cur.left = self.pre

            else:
                self.head = cur

            self.pre = cur
            dfs(cur.right)

        dfs(cur)

        self.head.left = self.pre
        self.pre.right = self.head

        return self.head


if __name__ == '__main__':
    Node4 = Node(4)
    Node2 = Node(2)
    Node5 = Node(5)
    Node1 = Node(1)
    Node3 = Node(3)

    Node4.left = Node2
    Node4.right = Node5
    Node2.left = Node1
    Node2.right = Node3

    print( Solution().treeToDoublyList(Node4) )

