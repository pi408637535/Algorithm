# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 16:41
# @Author  : piguanghua
# @FileName: Maximun_Depth_Of_Binary_Tree.py
# @Software: PyCharm
import math

class BinaryTree():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        print("val={0},left={1}, right={2}"
              .format(self.value, self.left, self.right))


class Solution(object):
    def max_depth_binary_tree(node, depth):

        if node == None:
            return depth
        else:
            depth += 1

        left = max_depth_binary_tree(node.left, depth)
        right = max_depth_binary_tree(node.right, depth)

        return left if left > right else right

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        data = max_depth_binary_tree(root, 0)
        return data


#Todo 不好的分治算法.利用了全局变量
def max_depth_binary_tree(node, depth):



    if node == None:
        return depth
    else:
        depth += 1

    left = max_depth_binary_tree(node.left, depth)
    right = max_depth_binary_tree(node.right, depth)

    return left if left > right else right


#改良版
def max_depth_binary_tree2(node):

    if node == None:
        return 0


    leftDepth = max_depth_binary_tree2(node.left)
    rightDepth = max_depth_binary_tree2(node.right)

    return max(leftDepth, rightDepth) + 1

#Todo Maximum Depth of Binary Tree传入结构是[],并非二叉树。后期需要改

if __name__ == '__main__':
    node1 = BinaryTree(1)
    node2 = BinaryTree(2)
    node3 = BinaryTree(3)
    node4 = BinaryTree(4)
    node5 = BinaryTree(5)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    data = max_depth_binary_tree(node1, 0)
    print(data)

    data = max_depth_binary_tree2(node1)
    print(data)


