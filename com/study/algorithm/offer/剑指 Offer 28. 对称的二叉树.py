
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

    def helper(self, root):

        if root == None:
            return ResultType(True, None)

        left_result = self.helper(root.left)
        right_result = self.helper(root.right)

        if left_result.node == None and right_result.node == None:
            return ResultType(True, root)
        elif left_result.node == None or right_result.node == None:
            return ResultType(False, root)

        if left_result.node.val != right_result.node.val or left_result.is_same == False or \
            right_result.is_same == False:
            return ResultType(False, root)
        else:
            return ResultType(True, root)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result_type = self.helper(root)
        return result_type.is_same


if __name__ == '__main__':
    TreeNode1 = TreeNode(1)
    TreeNode2_1 = TreeNode(2)
    TreeNode2_2 = TreeNode(2)
    TreeNode3_1 = TreeNode(3)
    TreeNode3_2 = TreeNode(3)
    TreeNode4_1 = TreeNode(4)
    TreeNode4_2 = TreeNode(4)

    TreeNode1.left = TreeNode2_1
    TreeNode1.right = TreeNode2_2
    TreeNode2_1.left = TreeNode3_1
    TreeNode2_1.right = TreeNode4_1
    TreeNode2_2.left = TreeNode4_2
    TreeNode2_2.right = TreeNode3_2

    print( Solution().isSymmetric(TreeNode1) )





