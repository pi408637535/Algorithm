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




class Solution(object):

    def helper(self, node):

        if node == None:
            return 0

        left_depth = self.helper(node.left)
        right_depth = self.helper(node.right)

        return left_depth + 1 if left_depth > right_depth else right_depth + 1



    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return True
        else:
            leftHigh =  self.helper(root.left)
            rightHigh = self.helper(root.right)

      
        if abs( leftHigh - rightHigh  ) > 1:
            return False
        else:
            return True

class InnerValue(object):
    def __init__(self, high, is_balance):
        self.high = high
        self.is_balance = is_balance

class Solution2(object):

    def helper(self, node):

        if node == None:
            return InnerValue(0, True)

        left = self.helper(node.left)
        right = self.helper(node.right)

        if ( not left.is_balance or not right.is_balance):
            return InnerValue(-1,False)

        if abs( left.high - right.high ) > 1:
            return InnerValue(-1, False)

        return InnerValue( max(left.high, right.high)+1 , True)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        data = self.helper(root).is_balance
        return data.is_balance



if __name__ == '__main__':


    node1 = TreeNode(1)
    node2_1 = TreeNode(2)
    node2_2 = TreeNode(2)
    node3_1 = TreeNode(3)
    node3_2 = TreeNode(3)
    node4_1 = TreeNode(4)
    node4_2 = TreeNode(4)

    node1.left = node2_1
    node1.right = node2_2

    node2_1.left = node3_1
    node2_1.right = node3_2

    node3_1.left = node4_1
    node3_1.right = node4_2


    '''
    node1 = TreeNode(1)
    node2_1 = TreeNode(2)
    node2_2 = TreeNode(2)
    node3_1 = TreeNode(3)
    node3_2 = TreeNode(3)
    node4_1 = TreeNode(4)
    node4_2 = TreeNode(4)

    node1.left = node2_1
    node1.right = node2_2
    node2_1.left = node3_1
    node2_2.right = node3_2
    node3_1.left = node4_1
    node3_2.right = node4_2
    '''

    '''
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node7
    '''

    print( Solution2().isBalanced(node1) )


