# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 09:40
# @Author  : piguanghua
# @FileName: 剑指 Offer 54. 二叉搜索树的第k大节点.py
# @Software: PyCharm


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        data = []
        self.k = k
        self.res = 0

        def in_order(root):
            if root != None:
                in_order(root.right)
                if self.k == 0: return
                self.k -= 1
                if self.k == 0: self.res = root.val
                data.append(root.val)
                in_order(root.left)

        in_order(root)
        return self.res


if __name__ == '__main__':
    TreeNode3 = TreeNode(3)
    TreeNode1 = TreeNode(1)
    TreeNode4 = TreeNode(4)
    TreeNode2 = TreeNode(2)

    TreeNode3.left = TreeNode1
    TreeNode3.right = TreeNode4
    TreeNode1.right = TreeNode2

    print(Solution().kthLargest(TreeNode3, 4))
