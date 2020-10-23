
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype
        """
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max([ left_depth, right_depth ]) + 1

class Solution(object):

    def helper(self, root, k):
        stack = []

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            k -= 1
            temp = stack.pop()
            if not k:
                return temp.val
            root = temp.right


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None

        return self.helper(root, k)


if __name__ == '__main__':
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node17 = TreeNode(17)

    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node17

    print(Solution().maxDepth(node3))

