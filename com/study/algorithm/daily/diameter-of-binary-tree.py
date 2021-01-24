'''
    树基本是递归。
    递归：四要素
    本题思路:left+right=diameter
    https://www.lintcode.com/problem/diameter-of-binary-tree/description
'''
#思路：
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


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

if __name__ == '__main__':
    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)
    TreeNode3 = TreeNode(3)
    TreeNode4 = TreeNode(4)
    TreeNode5 = TreeNode(5)

    TreeNode1.left = TreeNode2
    TreeNode1.right = TreeNode3
    TreeNode2.left = TreeNode4
    TreeNode2.right = TreeNode5

    # TreeNode1 = TreeNode(1)
    # TreeNode2 = TreeNode(2)
    # TreeNode3 = TreeNode(3)
    #
    # TreeNode2.left = TreeNode3
    # TreeNode3.left = TreeNode1

    print(Solution().diameterOfBinaryTree(TreeNode1))

