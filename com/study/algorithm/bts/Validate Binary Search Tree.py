# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 11:10
# @Author  : piguanghua
# @FileName: Validate Binary Search Tree.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

import sys
class ResultType(object):
    def __init__(self, left_max, right_min):
        self.left_max = left_max
        self.right_min = right_min


class Solution(object):
    def __init__(self):
       self.data = []

    def helper(self, root):
        if root != None:
            self.helper(root.left)
            self.data.append(root.val)
            self.helper(root.right)

    def judge(self):
        if len(self.data) == 1:
            return True
        else:
            j = 1
            for i in range(len(self.data) - 1):
                if self.data[i] > self.data[j]:
                    return False
                j += 1

            for i in range(len(self.data)-1, 0, -1):
                j = i - 1
                if self.data[i] <= self.data[j]:
                    return False

            return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.helper(root)
        return self.judge()


class Solution1(object):

    def helper(self, root):
        if root == None:
            return ResultType(True, -sys.maxsize, sys.maxsize)


        left = self.helper(root.left)
        right = self.helper(root.right)

        if not left.result or not right.result:
            return ResultType(False, 0, 0)

        if root.left != None and root.right != None:
            if left.left_max >= root.val or right.right_min <= root.val:
                return ResultType(False, 0, 0)
            else:
                return ResultType(True, max([root.val, left.left_max]), min([root.val, right.right_min]))

        elif  root.left != None:
            if left.max_value >= root.val:
                return ResultType(False, 0, 0)
            else:
                return ResultType(True, max([root.val, left.left_max]), root.val)

        elif  root.right != None:
            if right.min_value <= root.val:
                return ResultType(False, 0, 0)
            else:
                return ResultType(True, root.val, min([root.val, right.right_min]))

        else:
            return ResultType(True, root.val, root.val)


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root).result



if __name__ == '__main__':
    '''
    TreeNode5 = TreeNode(5)
    TreeNode1 = TreeNode(1)
    TreeNode4 = TreeNode(4)
    TreeNode3 = TreeNode(3)
    TreeNode6 = TreeNode(6)

    TreeNode5.left = TreeNode1
    TreeNode5.right = TreeNode4
    TreeNode4.left = TreeNode3
    TreeNode4.right = TreeNode6
'''

    '''
    TreeNode10 = TreeNode(10)
    TreeNode5 = TreeNode(5)
    TreeNode15 = TreeNode(15)
    TreeNode6 = TreeNode(6)
    TreeNode20 = TreeNode(20)
    TreeNode10.left = TreeNode5
    TreeNode10.right = TreeNode15
    TreeNode15.left = TreeNode6
    TreeNode15.right = TreeNode20
    #TreeNode5.right = TreeNode9
    '''

    '''
    
    TreeNode2 = TreeNode(2)
    TreeNode1 = TreeNode(1)
    TreeNode3 = TreeNode(3)
    TreeNode2.left = TreeNode1
    TreeNode2.right = TreeNode3
    '''

    '''
    TreeNode_59 = TreeNode(-59)
    TreeNode49 = TreeNode(49)
    TreeNode78 = TreeNode(78)
    TreeNode_59.right = TreeNode49
    TreeNode49.right = TreeNode78
    '''
    TreeNode1 = TreeNode(1)
    TreeNode_1 = TreeNode(1)
    TreeNode1.right = TreeNode_1

    print( Solution().isValidBST(TreeNode1) )
