
import collections

class ResultType():
    def __init__(self, is_same, node):
        self.is_same = is_same
        self.node = node

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def bfs(left, right):
            if not left and not right: return True
            if not left or not right or left.val != right.val:
                return False

            return bfs(left.left, right.right) and bfs(left.right, right.left)


        return  bfs(root.left, root.right) if root else True


if __name__ == '__main__':
    TreeNode1 = TreeNode(1)
    TreeNode2_1 = TreeNode(2)
    TreeNode2_2 = TreeNode(2)
    TreeNode3_1 = TreeNode(3)
    TreeNode3_2 = TreeNode(3)
    TreeNode4_1 = TreeNode(4)
    TreeNode4_2 = TreeNode(4)

    # TreeNode1.left = TreeNode2_1
    # TreeNode1.right = TreeNode2_2
    # TreeNode2_1.left = TreeNode3_1
    # TreeNode2_1.right = TreeNode4_1
    # TreeNode2_2.left = TreeNode4_2
    # TreeNode2_2.right = TreeNode3_2

    TreeNode1.left = TreeNode2_1
    TreeNode1.right = TreeNode2_2
    TreeNode2_1.right = TreeNode3_1
    TreeNode2_2.right = TreeNode3_2

    print( Solution().isSymmetric(TreeNode1) )





