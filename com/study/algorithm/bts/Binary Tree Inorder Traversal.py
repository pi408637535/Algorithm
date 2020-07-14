class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):

    def __init__(self):
        self.data = []


    def helper(self, root):
        if root != None:
            self.helper(root.left)
            self.data.append( root.val )
            self.helper(root.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root)
        return self.data

if __name__ == '__main__':
    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)
    TreeNode3 = TreeNode(3)

    TreeNode1.right = TreeNode2
    TreeNode2.left = TreeNode3

    print( Solution().inorderTraversal(TreeNode1) )
