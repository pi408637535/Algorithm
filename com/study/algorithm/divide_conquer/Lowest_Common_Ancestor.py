


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

#idea: 因为所有点不同且所有点都在二叉树内，那么可以从顶层->底层逐层查找。只要顶层的点==p or q，那么久找到了

class Solution(object):

    def helper(self, node, p, q):

        if node == None:
            return None

        if node.val == p.val or node.val == q.val:
            return node


        #div
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)

        #conquer
        if left != None and right != None: #left,riht
            return node

        if left == None and right != None: #right
            return  right

        if left != None and right == None: #left
            return left

        return None




    def lowestCommonAncestor(self, root, p ,q):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.helper(root,p,q)

if __name__ == '__main__':
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node7 = TreeNode(7)
    node4 = TreeNode(4)

    node3.left = node5
    node3.right = node1
    node5.left = node6
    node5.right = node2
    node1.left = node0
    node1.right = node8
    node2.left = node7
    node2.right = node4

    print( Solution().lowestCommonAncestor(node3, p = node5, q = node4) )

