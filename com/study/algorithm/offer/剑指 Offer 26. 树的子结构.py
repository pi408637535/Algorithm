class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def dfs(self, A, B):
        if not B:
            return True

        if not A or A.val != B.val:
            return False

        return self.dfs(A.left, B.left) and self.dfs(A.right, B.right)

    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """

        return bool(A and B) and \
               (self.dfs(A, B) or
                self.isSubStructure(A.left, B) or
                self.isSubStructure(A.right, B))




if __name__ == '__main__':
    TreeNode3 = TreeNode(3)
    TreeNode4_1 = TreeNode(4)
    TreeNode5 = TreeNode(5)
    TreeNode1_1 = TreeNode(1)
    TreeNode2 = TreeNode(2)

    TreeNode3.left = TreeNode4_1
    TreeNode3.right = TreeNode5
    TreeNode4_1.left = TreeNode1_1
    TreeNode4_1.right = TreeNode2

    TreeNode4_2 = TreeNode(4)
    TreeNode1_2 = TreeNode(1)
    TreeNode4_2.left = TreeNode1_2

    # TreeNode1_1 = TreeNode(1)
    # TreeNode0 = TreeNode(0)
    # TreeNode1_2 = TreeNode(1)
    # TreeNode_4_1 = TreeNode(-4)
    # TreeNode_3 = TreeNode(-3)
    # TreeNode1_1.left = TreeNode0
    # TreeNode1_1.right = TreeNode1_2
    # TreeNode0.left = TreeNode_4_1
    # TreeNode0.right = TreeNode_3
    #
    # TreeNode1_3 = TreeNode(1)
    # TreeNode_4_2 = TreeNode(-4)
    #
    # TreeNode1_3.left = TreeNode_4_2

    print(Solution().isSubStructure(TreeNode3, TreeNode4_2))


