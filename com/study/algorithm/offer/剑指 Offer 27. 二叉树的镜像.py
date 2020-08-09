class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return None

        left_root = self.mirrorTree(root.left)
        right_root = self.mirrorTree(root.right)

        new_node = TreeNode(root.val)
        new_node.left = right_root
        new_node.right = left_root

        return new_node



if __name__ == '__main__':
    pass