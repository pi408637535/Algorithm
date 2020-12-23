# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class LevelSolution(object):
    def levelOrder(self, root):
        """
       :type root: TreeNode
       :rtype: List[List[int]]
       """
        queue = collections.deque()
        if not root:
            return []
        else:
            queue.append(root)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res



class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()

        if not root:
             return []
        else:
            queue.append(root)

        res = []
        flag = 1 # 1 left,0 right 用于标识左右遍历的方向
        while queue:

            #要全部弹出
            temp = []
            for i in range(len(queue)):
                temp.append(queue.popleft())

            if flag:
                res.append( [ele.val for ele in temp] )
            else:
                res.append([ele.val for ele in temp[::-1]] )

            for ele in temp:
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)

            flag = 1 - flag
        return res



if __name__ == '__main__':
    TreeNode3 = TreeNode(3)
    TreeNode9 = TreeNode(9)
    TreeNode20 = TreeNode(20)
    TreeNode15 = TreeNode(15)
    TreeNode7 = TreeNode(7)

    TreeNode3.left = TreeNode9
    TreeNode3.right = TreeNode20
    TreeNode20.left = TreeNode15
    TreeNode20.right = TreeNode7

    print(LevelSolution().levelOrder(TreeNode3))
    # print(Solution().zigzagLevelOrder(TreeNode3))

