class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        res_value = sum - root.val

        if not res_value and not root.left and not root.right:
            return True

        left_result = self.hasPathSum(root.left, res_value)
        right_result = self.hasPathSum(root.right, res_value)

        return left_result or right_result
