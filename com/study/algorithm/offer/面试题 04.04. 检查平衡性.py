# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ResultType():
    def __init__(self, balance, height):
        self.balance = balance
        self.height = height


class Solution(object):

    def helper(self, root):
        if not root:
            return ResultType(True, 1)

        left = self.helper(root.left)
        right = self.helper(root.right)

        is_balance = True
        if not left.balance or not right.balance or abs(left.height - right.height)  > 1:
            is_balance = False

        return ResultType(is_balance, max(left.height, right.height)  + 1 )



    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = self.helper(root)

        return result.balance
