# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 16:49
# @Author  : piguanghua
# @FileName: 剑指 Offer 34. 二叉树中和为某一值的路径.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum_total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(root, sum_total, cur):
            if root != None:
                if sum_total - root.val == 0:
                    cur.append(root.val)
                    ans.append(cur.copy())
                    cur.pop()
                    return

                if sum_total - root.val > 0:
                    cur.append(root.val)
                    sum_total -= root.val

                    dfs(root.left, sum_total, cur)
                    dfs(root.right, sum_total, cur)

                    data = cur.pop()
                    sum_total += data


        dfs(root, sum_total, [])

        return ans






if __name__ == '__main__':
    TreeNode5_1 = TreeNode(5)
    TreeNode4_1 = TreeNode(4)
    TreeNode4_2 = TreeNode(4)

    TreeNode8 = TreeNode(8)
    TreeNode11 = TreeNode(11)
    TreeNode13 = TreeNode(13)
    TreeNode4 = TreeNode(4)
    TreeNode7 = TreeNode(7)
    TreeNode2 = TreeNode(2)
    TreeNode5_2 = TreeNode(5)
    TreeNode1 = TreeNode(1)

    TreeNode5_1.left = TreeNode4_1
    TreeNode5_1.right = TreeNode8
    TreeNode4_1.left = TreeNode11
    TreeNode8.left = TreeNode13
    TreeNode8.right = TreeNode4_2
    TreeNode11.left = TreeNode7
    TreeNode11.right = TreeNode2
    TreeNode4_2.left = TreeNode5_2
    TreeNode4_2.right = TreeNode1

    print( Solution().pathSum(TreeNode5_1, 22) )

