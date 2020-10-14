# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def helper(self, root):
        if root:
            self.helper(root.left)
            self.res.append(root.val)
            self.helper(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = []
        self.helper(root)

        if len(self.res) == 0 or len(self.res) == 1:
            return True

        slow = 0
        fast = 1
        while fast < len(self.res):
            if self.res[slow] >= self.res[fast]:
                return False
            slow += 1
            fast += 1
        return True

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        pre = None
        while stack or root:

            while root:
                stack.append(root)
                root = root.left

            temp = stack.pop()

            if not pre:
                pre = temp
            else:
                if pre.val >= temp.val:
                    return False
                pre = temp

            root = temp.right

        return True

if __name__ == '__main__':
    '''
    TreeNode2 = TreeNode(2)
    TreeNode1 = TreeNode(1)
    TreeNode3 = TreeNode(3)

    TreeNode2.left = TreeNode1
    TreeNode2.right = TreeNode3


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

    TreeNode1_1 = TreeNode(1)
    TreeNode1_2 = TreeNode(1)
    TreeNode1_1.left = TreeNode1_2

    print(Solution().isValidBST(TreeNode1_1))



