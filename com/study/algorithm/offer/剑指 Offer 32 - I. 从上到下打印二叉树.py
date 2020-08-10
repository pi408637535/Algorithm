# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 14:20
# @Author  : piguanghua
# @FileName: 剑指 Offer 32 - I. 从上到下打印二叉树.py
# @Software: PyCharm


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution(object):

    def __init__(self):
        self.queue = []

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        data_order = collections.deque()
        data_order.append(root)
        data_val = []

        while data_order:
            node = data_order.popleft()
            data_val.append(node.val)

            if node.left != None:
                data_order.append(node.left)
            if node.right != None:
                data_order.append(node.right)

        return data_val


if __name__ == '__main__':
    pass