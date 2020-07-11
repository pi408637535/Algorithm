
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):

    def __init__(self):
        self.max = 0

    def helper(self, root, depth):

        if root == None:
            return
        self.max = max( [self.max,depth ])
        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        self.helper(root, 1)

        return self.max

class Solution1(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)



        return max( [left_depth, right_depth] ) + 1


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

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.left = node2

    print( Solution1().maxDepth(node1) )

