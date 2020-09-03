# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 11:04
# @Author  : piguanghua
# @FileName: Symmetric Tree.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def helper(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val == q.val:
            left_result = self.helper(p.left, q.right)
            right_result = self.helper(p.right, q.left)
            return left_result and right_result
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.helper(root.left, root.right)





if __name__ == '__main__':
    pass