class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.dic = {}
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        root = self.helper(preorder, 0, inorder, 0, len(inorder) - 1)
        return root


    def helper(self, preorder, root_index, inorder, left_index, right_index):

        if left_index > right_index:
            return None


        root = TreeNode(preorder[root_index])

        sub_tree_index = self.dic[preorder[root_index]]

        root.left = self.helper(preorder, root_index + 1, inorder, left_index, sub_tree_index - 1 )
        #root.right = self.helper(preorder, sub_tree_index - left_index + root_index + 1, inorder, sub_tree_index + 1, right_index)
        root.right = self.helper(preorder, root_index + 1 +  sub_tree_index - left_index, inorder, sub_tree_index + 1,
                                 right_index)
        #sub_tree_index - left_index 表示 左子树现有的个数
        #root_index + 1 左子树现在根所在的位置
        #sub_tree_index - left_index + root_index + 1 右子树现在根所在的位置

        return root


class Solution(object):

    def helper(self, preorder, root_index, inorder, left_index, right_index):
        if left_index > right_index:
            return None

        root = TreeNode(preorder[root_index])

        root_in_inoder_index = self.dic[preorder[root_index]]

        root.left = self.helper(preorder, root_index + 1, inorder, left_index, root_in_inoder_index - 1)
        root.right = self.helper(preorder, root_index + 1 + root_in_inoder_index - left_index, inorder,
                                 root_in_inoder_index + 1, right_index)

        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        self.dic = {}
        for index, ele in enumerate(inorder):
            self.dic[ele] = index
        left_index = 0
        right_index = len(inorder) - 1
        root = self.helper(preorder, 0, inorder, left_index, right_index)
        return root


if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    preorder = [1,2]
    inorder = [1,2]

    print( Solution().buildTree(preorder, inorder) )
