# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 10:03
# @Author  : piguanghua
# @FileName: Path Sum.py
# @Software: PyCharm


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        if sum - root.val == 0 and root.left == None and root.right == None:
            return True
        elif sum - root.val < 0 and root.left == None and root.right == None:
            return False


        rest_value = sum - root.val

        left_result = self.hasPathSum(root.left, rest_value)
        right_result = self.hasPathSum(root.right, rest_value)

        return left_result or right_result


if __name__ == '__main__':
    TreeNode5 = TreeNode(5)
    TreeNode4_1 = TreeNode(4)
    TreeNode8 = TreeNode(8)
    TreeNode11 = TreeNode(11)
    TreeNode13 = TreeNode(13)
    TreeNode4_2 = TreeNode(4)
    TreeNode7 = TreeNode(7)
    TreeNode2 = TreeNode(2)
    TreeNode1 = TreeNode(1)

    TreeNode5.left = TreeNode4_1
    TreeNode5.right = TreeNode8
    TreeNode4_1.left = TreeNode11
    TreeNode8.left = TreeNode13
    TreeNode8.right = TreeNode4_2
    TreeNode11.left = TreeNode7
    TreeNode11.right = TreeNode2
    TreeNode4_2.right = TreeNode1

    # TreeNode_2 = TreeNode(-2)
    # TreeNode_3 = TreeNode(-3)
    # TreeNode_2.right = TreeNode_3


    print(Solution().hasPathSum(TreeNode5, 22))



