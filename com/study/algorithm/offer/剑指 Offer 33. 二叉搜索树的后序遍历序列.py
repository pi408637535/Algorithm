# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 16:05
# @Author  : piguanghua
# @FileName: 剑指 Offer 33. 二叉搜索树的后序遍历序列.py
# @Software: PyCharm

#BTS后序遍历 left-right-root,
#由于BTS性质，left < root, right > root,所以对于给定的后序遍历，看该序列是否是BTS，简单的方法
#就是判断 左< root, 右边 > root,个子树，逐一确定就行
# 终止条件: left_index >= right 单一节点或叶子节点。 返回 True

class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """

        def cur(left, right):
            if left >= right: return True

            p = left
            while postorder[p] < postorder[right]:
                p += 1
            m = p
            while postorder[p] > postorder[right]:
                p += 1

            return p == right and cur(left, m-1) and cur(m, right-1)

        return cur(0, len(postorder) - 1)


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if len(postorder) == 1 or not postorder:
            return True


        split_line = 0
        while postorder[split_line] < postorder[-1]:
            split_line += 1
        left_tree = postorder[:split_line]
        right_tree = postorder[split_line:len(postorder)-1]

        left_result = True
        for ele in left_tree:
            if ele > postorder[-1]: left_result = False
        right_result = True
        for ele in right_tree:
            if ele < postorder[-1]: right_result = False

        return self.verifyPostorder(left_tree) and self.verifyPostorder(right_tree) and left_result and right_result


if __name__ == '__main__':
    postorder = [1,3,2,6,5]
    print( Solution().verifyPostorder(postorder) )