# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 13:46
# @Author  : piguanghua
# @FileName: Lowest Common Ancestor of a Binary Tree.py
# @Software: PyCharm


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.current_depth = 0
        self.pre_lca = None
        self.cur_lca = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        if right_lca == None and left_lca != None:
            return left_lca
        elif left_lca == None and right_lca != None:
            return right_lca
        elif right_lca != None and left_lca != None:
            return root
        else:
            return None






if __name__ == '__main__':
    TreeNode3 = TreeNode(3)
    TreeNode5 = TreeNode(5)
    TreeNode1 = TreeNode(1)
    TreeNode6 = TreeNode(6)
    TreeNode2 = TreeNode(2)
    TreeNode0 = TreeNode(0)
    TreeNode8 = TreeNode(8)
    TreeNode7 = TreeNode(7)
    TreeNode4 = TreeNode(4)

    TreeNode3.left = TreeNode5
    TreeNode3.right = TreeNode1
    TreeNode5.left  = TreeNode6
    TreeNode5.right = TreeNode2
    TreeNode1.left = TreeNode0
    TreeNode1.right = TreeNode8
    TreeNode2.left = TreeNode7
    TreeNode4.right = TreeNode4

    
    print( Solution().lowestCommonAncestor(TreeNode3, TreeNode5, TreeNode1) )
