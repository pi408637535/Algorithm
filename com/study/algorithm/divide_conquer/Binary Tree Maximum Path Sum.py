# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 17:35
# @Author  : piguanghua
# @FileName: Binary Tree Maximum Path Sum.py
# @Software: PyCharm
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return -sys.maxsize

        left_max = self.maxPathSum(root.left)
        right_max = self.maxPathSum(root.right)

        return max( [ left_max, right_max, \
                      (left_max + right_max + root.val), left_max + root.val, right_max + root.val ] )



if __name__ == '__main__':
    TreeNode_10 = TreeNode(-10)
    TreeNode9 = TreeNode(9)
    TreeNode20 = TreeNode(20)
    TreeNode15 = TreeNode(15)
    TreeNode7 = TreeNode(7)

    TreeNode_10.left = TreeNode9
    TreeNode_10.right = TreeNode20
    TreeNode20.left = TreeNode15
    TreeNode20.right = TreeNode7

    print( Solution().maxPathSum(TreeNode_10) )
