# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 10:52
# @Author  : piguanghua
# @FileName: Same Tree.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p or not q: return False

        if p.val == q.val:
            left_result = self.isSameTree(p.left, q.left)
            right_result = self.isSameTree(p.right, q.right)

            return left_result and right_result

        else:
            return False

if __name__ == '__main__':
    pass