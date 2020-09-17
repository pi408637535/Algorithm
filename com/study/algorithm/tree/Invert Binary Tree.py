class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right,left

        return root


if __name__ == '__main__':
    TreeNode4 = TreeNode(4)
    TreeNode2 = TreeNode(2)
    TreeNode7 = TreeNode(7)
    TreeNode1 = TreeNode(1)
    TreeNode3 = TreeNode(3)
    TreeNode6 = TreeNode(6)
    TreeNode9 = TreeNode(9)

    TreeNode4.left = TreeNode2
    TreeNode4.right = TreeNode7

    TreeNode2.left = TreeNode1
    TreeNode2.right = TreeNode3

    TreeNode7.left = TreeNode6
    TreeNode7.right = TreeNode9

    print(Solution().invertTree(TreeNode4))




