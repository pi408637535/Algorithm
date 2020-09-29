class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left_node = self.lowestCommonAncestor(root.left, p, q)
        #right_node = self.helper(root.right, p.val, q.val)
        right_node = self.lowestCommonAncestor(root.right, p, q)

        if left_node == None and right_node != None:
            return right_node
        elif right_node == None and left_node != None:
            return left_node
        elif left_node != None and right_node != None:
            return root
        else:
            return None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None
        if root == p or root == q:
            return root

        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        if not left_res and right_res:
            return right_res
        elif not right_res and left_res:
            return left_res
        elif left_res and right_res:
            return root




if __name__ == '__main__':
    TreeNode3 = TreeNode(3)
    TreeNode5 = TreeNode(5)
    TreeNode1 = TreeNode(1)
    TreeNode6 = TreeNode(6)
    TreeNode2 = TreeNode(2)
    TreeNode0 = TreeNode(0)
    TreeNode8 = TreeNode(8)
    TreeNode7 = TreeNode(7)
    TreeNode4 = TreeNode(4)

    TreeNode3.left = TreeNode5
    TreeNode3.right = TreeNode1
    TreeNode5.left = TreeNode6
    TreeNode5.right = TreeNode2
    TreeNode1.left = TreeNode0
    TreeNode1.right = TreeNode8
    TreeNode2.left = TreeNode7
    TreeNode4.right = TreeNode4

    print(Solution().lowestCommonAncestor(TreeNode3, TreeNode5, TreeNode2))