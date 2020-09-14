# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys


class Solution(object):

    def helper(self, root):

        if not root:
            return -sys.maxsize

        left = max([self.helper(root.left), 0])
        right = max([self.helper(root.right), 0])

        self.max_size = max([root.val + left + right, self.max_size])

        return max([root.val, root.val + right, root.val + left])

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        self.max_size = -sys.maxsize

        self.helper(root)

        return self.max_size


class ResultType():
    def __init__(self, root2any, any2any):
        self.root2any = root2any
        self.any2any = any2any


import sys


class Solution(object):

    def helper(self, root):

        if not root:
            return ResultType(-sys.maxsize, -sys.maxsize)

        left = self.helper(root.left)
        right = self.helper(root.right)

        root2any = max([root.val, root.val + max(0, left.root2any),
                        root.val + max(0, right.root2any)])

        any2any = max([root2any, root.val + max(0, left.root2any)
                       + max(0, right.root2any),
                       left.any2any,
                       right.any2any])

        return ResultType(root2any, any2any)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = self.helper(root)

        return result.any2any

if __name__ == '__main__':
    TreeNode1= TreeNode(1)
    TreeNode_2_1 = TreeNode(-2)
    TreeNode_3 = TreeNode(-3)
    TreeNode1_1 = TreeNode(1)
    TreeNode3 = TreeNode(3)
    TreeNode_2_2 = TreeNode(-2)
    TreeNode1_2 = TreeNode(-1)

    TreeNode1.left = TreeNode_2_1
    TreeNode1.right = TreeNode_3
    TreeNode_2_1.left = TreeNode1_1
    TreeNode_2_1.right = TreeNode3
    TreeNode_3.left = TreeNode_2_2
    TreeNode1_1.left = TreeNode1_2

    print(Solution().maxPathSum(TreeNode1))

