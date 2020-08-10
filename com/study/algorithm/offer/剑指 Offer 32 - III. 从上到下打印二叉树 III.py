# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 15:39
# @Author  : piguanghua
# @FileName: 剑指 Offer 32 - III. 从上到下打印二叉树 III.py
# @Software: PyCharm


class TreeNode:
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
        i = 0

        while data_order:


            tmp = []

            i = int((i + 1) % 2)

            for _ in range(len(data_order)):

                node = data_order.popleft()
                tmp.append(node.val)

                if i == 1:
                    if node.right:
                        data_order.append(node.right)
                    if node.left:
                        data_order.append(node.left)
                else:

                    if node.left:
                        data_order.append(node.left)

                    if node.right:
                        data_order.append(node.right)

            data_val.append(tmp)


        return data_val


if __name__ == '__main__':
    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)
    TreeNode3 = TreeNode(3)
    TreeNode4 = TreeNode(4)
    TreeNode5 = TreeNode(5)

    TreeNode1.left = TreeNode2
    TreeNode1.right = TreeNode3
    TreeNode2.left = TreeNode4
    TreeNode3.right = TreeNode5

    print( Solution().levelOrder(TreeNode1) )

