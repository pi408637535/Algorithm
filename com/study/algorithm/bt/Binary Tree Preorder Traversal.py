# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 15:39
# @Author  : piguanghua
# @FileName: Binary Tree Preorder Traversal.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):

    def __init__(self):
        self.data = []

    def helper(self, node):
        if node != None:
            self.data.append(node.val)
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root)
        return self.data


if __name__ == '__main__':
    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)
    TreeNode3 = TreeNode(3)
    TreeNode1.right = TreeNode2
    TreeNode2.left = TreeNode3

    print(Solution().preorderTraversal(TreeNode1))
