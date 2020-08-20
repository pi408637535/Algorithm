# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys

class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_num = -sys.maxsize
        def helper(root):
            if root == None:
                return max_num

            left_num = helper(root.left)
            right_num = helper(root.right)

            
            return max([left_num, right_num, root.val, root.val + left_num,
                        root.val + right_num, root.val + left_num + right_num
                        ])

        if root == None:
            return 0
        
        return helper(root)
        

if __name__ == '__main__':
    TreeNode1= TreeNode(1)
    TreeNode_2_1 = TreeNode(-2)
    TreeNode_3 = TreeNode(-3)
    TreeNode1_1 = TreeNode(1)
    TreeNode3 = TreeNode(3)
    TreeNode_2_2 = TreeNode(-2)
    TreeNode1_2 = TreeNode(-1)

    TreeNode1.left = TreeNode_2_1
    TreeNode1.right = TreeNode_3
    TreeNode_2_1.left = TreeNode1_1
    TreeNode_2_1.right = TreeNode3
    TreeNode_3.left = TreeNode_2_2
    TreeNode1_1.left = TreeNode1_2

    print(Solution().maxPathSum(TreeNode1))

