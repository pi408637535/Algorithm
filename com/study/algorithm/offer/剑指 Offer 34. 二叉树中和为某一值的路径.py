# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 16:49
# @Author  : piguanghua
# @FileName: 剑指 Offer 34. 二叉树中和为某一值的路径.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import copy
class Solution(object):
    def pathSum(self, root, sums):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ans = []

        def helper(root, num, res):

            if not root:
                return

            res.append(root.val)

            if num - root.val == 0 and not root.left and not root.right:
                self.ans.append(copy.copy(res))

            helper(root.left, num - root.val, res)
            helper(root.right, num - root.val, res)
            res.pop()

        helper(root, sums, [])
        return self.ans





if __name__ == '__main__':
    TreeNode5_1 = TreeNode(5)
    TreeNode4_1 = TreeNode(4)
    TreeNode4_2 = TreeNode(4)

    TreeNode8 = TreeNode(8)
    TreeNode11 = TreeNode(11)
    TreeNode13 = TreeNode(13)
    TreeNode4 = TreeNode(4)
    TreeNode7 = TreeNode(7)
    TreeNode2 = TreeNode(2)
    TreeNode5_2 = TreeNode(5)
    TreeNode1 = TreeNode(1)

    TreeNode5_1.left = TreeNode4_1
    TreeNode5_1.right = TreeNode8
    TreeNode4_1.left = TreeNode11
    TreeNode8.left = TreeNode13
    TreeNode8.right = TreeNode4_2
    TreeNode11.left = TreeNode7
    TreeNode11.right = TreeNode2
    TreeNode4_2.left = TreeNode5_2
    TreeNode4_2.right = TreeNode1

    print( Solution().pathSum(TreeNode5_1, 22) )

