

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """

        def dfs(tree, sub_tree):
            if not sub_tree: return True
            if not tree or tree.val != sub_tree.val: return False

            return dfs(tree.left, sub_tree.left) and dfs(tree.right, sub_tree.right)

        return bool(A and B) and (dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

if __name__ == '__main__':
    pass