# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 15:39
# @Author  : piguanghua
# @FileName: 剑指 Offer 32 - III. 从上到下打印二叉树 III.py
# @Software: PyCharm
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()

        if root:
            queue.append(root)

        res = []
        i = 1
        while queue:

            nodos = []

            while queue:
                nodos.append(queue.popleft())

            tmp = []

            for ele in nodos:

                if ele.left:
                    queue.append(ele.left)

                if ele.right:
                    queue.append(ele.right)

                tmp.append(ele.val)

            if i % 2 != 0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            i += 1
        return res

if __name__ == '__main__':
    # TreeNode3 = TreeNode(3)
    # TreeNode9 = TreeNode(9)
    # TreeNode20 = TreeNode(20)
    # TreeNode15 = TreeNode(15)
    # TreeNode7 = TreeNode(7)
    #
    # TreeNode3.left = TreeNode9
    # TreeNode3.right = TreeNode20
    # TreeNode20.left = TreeNode15
    # TreeNode20.right = TreeNode7

    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)
    TreeNode3 = TreeNode(3)
    TreeNode4 = TreeNode(4)
    TreeNode5 = TreeNode(5)

    TreeNode1.left = TreeNode2
    TreeNode1.right = TreeNode3
    TreeNode2.left = TreeNode4
    TreeNode3.right = TreeNode5


    print(Solution().levelOrder(TreeNode1))