# Definition for a binary tree node.
import math
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class ReturnType():
    def __init__(self, is_balance, depth):
        self.is_balance = is_balance
        self.depth = depth

class Solution(object):

    def helper(self, node):
        if node == None:
            return ReturnType(True, 0)

        left = self.helper(node.left)
        right = self.helper(node.right)

        is_balance = True
        if not left.is_balance or not right.is_balance:
            is_balance = False

        if abs( left.depth - right.depth ) > 1:
            is_balance = False

        depth = max(left.depth, right.depth ) + 1

        return ReturnType(is_balance, depth)


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        return self.helper(root).is_balance


if __name__ == '__main__':
    TreeNode3 = TreeNode(3)
    TreeNode9 = TreeNode(9)
    TreeNode20 = TreeNode(20)
    TreeNode15 = TreeNode(15)
    TreeNode7 = TreeNode(7)

    TreeNode3.left = TreeNode9
    TreeNode3.right = TreeNode20
    TreeNode20.left = TreeNode15
    TreeNode20.right = TreeNode7

    '''---------------------------'''


    print( Solution().isBalanced(TreeNode3) )
