class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = []
        pre = None
        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            temp = stack.pop()
            if not pre:
                pre = temp
            else:
                if pre == p:
                    return temp
                pre = temp

            root = temp.right

        return None