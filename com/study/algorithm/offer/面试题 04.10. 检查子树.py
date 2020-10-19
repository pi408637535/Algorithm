# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def helper(self, t1, t2):
        if not t2:
            return True
        if not t1:
            return False

        if t1.val != t2.val:
            return False
        else:
            return self.helper(t1.left, t2.left) and self.helper(t1.right, t2.right)

    def checkSubTree(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: bool
        """
        if not t2:
            return True
        if not t1:
            return False

        return self.helper(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

