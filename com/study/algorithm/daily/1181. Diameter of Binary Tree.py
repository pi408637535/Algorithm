"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def helper(self, root):

        if not root:
            return 0

        left_depth = self.helper(root.left)
        right_depth = self.helper(root.right)

        depth = max(left_depth, right_depth) + 1
        return depth

    def diameterOfBinaryTree(self, root):
        # write your code here
        left_depth = self.helper(root.left)
        right_depth = self.helper(root.right)


        return left_depth + right_depth