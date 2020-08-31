class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#技巧，如何保证二叉树路径不被走两次
import sys
class Solution(object):
    def __init__(self):
        self.ans = -sys.maxsize

    def helper(self, root):
        if not root: return -sys.maxsize
        l = max([0, self.helper(root.left)])
        r = max([0, self.helper(root.right)])
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max([l, r])

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #self.ans = -sys.maxsize
        self.helper(root)
        return self.ans



if __name__ == '__main__':
    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)
    TreeNode3 = TreeNode(3)

    TreeNode1.left = TreeNode2
    TreeNode1.right = TreeNode3

    print(Solution().helper(TreeNode1))
