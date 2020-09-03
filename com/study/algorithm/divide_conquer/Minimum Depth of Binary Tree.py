# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 09:49
# @Author  : piguanghua
# @FileName: Minimum Depth of Binary Tree.py
# @Software: PyCharm


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if left_depth == 0 and right_depth != 0:
            return right_depth + 1
        elif left_depth != 0 and right_depth == 0:
            return left_depth + 1
        else:
            return min([left_depth, right_depth]) + 1


if __name__ == '__main__':
    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)

    TreeNode1.left = TreeNode2

    print(Solution().minDepth(TreeNode1))

