# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 17:45
# @Author  : piguanghua
# @FileName: Balanced_Binary_Tree.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import math




class Solution(object):

    class InnerValue(object):
        def __init__(self):
            self.high = 0
            self.isBalance = False



    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


        if root == None:
            return 0

        leftHigh = self.isBalanced(root.left)
        rightHigh = self.isBalanced(root.right)



        return max( [leftHigh, rightHigh] ) + 1


if __name__ == '__main__':
