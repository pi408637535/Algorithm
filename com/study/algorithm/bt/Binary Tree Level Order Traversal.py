# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 14:57
# @Author  : piguanghua
# @FileName: Binary Tree Level Order Traversal.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):

    def __init__(self):
        self.queue = []
        self.result = []



    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return None

        self.result.append([root.val])
        self.queue.append(root)

        while len(self.queue) != 0:

            queue_data = []
            while len(self.queue) != 0:
                queue_data.append(self.queue.pop(0))

            level_data = []
            for ele in queue_data:
                if ele.left != None:
                    self.queue.append(ele.left)
                    level_data.append(ele.left.val)
                if ele.right != None:
                    self.queue.append(ele.right)
                    level_data.append(ele.right.val)

            if len(level_data) != 0:
                self.result.append(level_data)

        return self.result

if __name__ == '__main__':
    '''
    TreeNode3 = TreeNode(3)
    TreeNode9 = TreeNode(9)
    TreeNode20 = TreeNode(20)
    TreeNode15 = TreeNode(15)
    TreeNode7 = TreeNode(7)
    
    TreeNode3.left = TreeNode9
    TreeNode3.right = TreeNode20
    TreeNode20.left = TreeNode15
    TreeNode20.right = TreeNode7
    '''

    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)
    TreeNode3 = TreeNode(3)
    TreeNode4 = TreeNode(4)
    TreeNode5 = TreeNode(5)
    TreeNode1.left = TreeNode2
    TreeNode1.right = TreeNode3
    TreeNode2.left = TreeNode4
    TreeNode3.right = TreeNode5

    print(Solution().levelOrder(TreeNode1))
