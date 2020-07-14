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

class ResultType(object):
    def __init__(self, root2any, any2any):
        self.root2any = root2any
        self.any2any = any2any

class Solution(object):

    def helper(self, root):
        if root == None:
            return ResultType(-sys.maxsize, -sys.maxsize)

        left = self.helper(root.left)
        right = self.helper(root.right)

        root2any = max([root.val, left.root2any + root.val, right.root2any + root.val])

        any2any = max([left.any2any, right.any2any])
        any2any = max([any2any, max([left.root2any, 0]) + max([0, right.root2any]) + root.val])

        return ResultType(root2any, any2any)


    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = self.helper(root)
        return max(result.root2any, result.any2any)



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

    TreeNode1 = TreeNode(1)
    TreeNode_2_1 = TreeNode(-2)
    TreeNode_3 = TreeNode(-3)
    TreeNode1C1 = TreeNode(1)
    TreeNode3 = TreeNode(3)
    TreeNode_2_2 = TreeNode(-2)
    TreeNode_1 = TreeNode(-1)
    TreeNode1.left = TreeNode_2_1
    TreeNode1.right = TreeNode_3
    TreeNode_2_1.left = TreeNode1C1
    TreeNode_2_1.right = TreeNode3
    TreeNode_3.left = TreeNode_2_2
    TreeNode1C1.left = TreeNode_1

    print( Solution().maxPathSum(TreeNode1) )
