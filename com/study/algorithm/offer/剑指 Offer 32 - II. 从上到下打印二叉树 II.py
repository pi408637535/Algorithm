# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 14:35
# @Author  : piguanghua
# @FileName: 剑指 Offer 32 - II. 从上到下打印二叉树 II.py
# @Software: PyCharm


import collections
class Solution(object):

    def __init__(self):
        self.queue = []

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        data_order = collections.deque()
        data_order.append(root)
        data_val = []

        while data_order:


            tmp = []

            for _ in range(len(data_order)):

                node = data_order.popleft()
                tmp.append(node.val)

                if node.left:
                    data_order.append(node.left)

                if node.right:
                    data_order.append(node.right)

            data_val.append(tmp)

        return data_val

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        res = []
        if root:
            queue.append(root)

        while len(queue):
            temp_res = []
            while queue:
                temp_res.append(queue.popleft())

            temp = []
            for ele in temp_res:
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                temp.append(ele.val)
            res.append(temp)



        return  res


if __name__ == '__main__':
    pass