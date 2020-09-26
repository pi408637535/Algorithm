
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ReturnType():
    def __init__(self, is_balance, high):
        self.is_balance = is_balance
        self.high = high

class Solution(object):

    def helper(self, root):
        if root == None:
            return ReturnType(True, 0)

        left_return = self.helper(root.left)
        right_return = self.helper(root.right)

        if abs(left_return.high - right_return.high) > 1 or left_return.is_balance == False or right_return.is_balance == False :
            return ReturnType(False, max([left_return.high, right_return.high]) + 1)
        else:
            return ReturnType(True, max([left_return.high, right_return.high]) + 1)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper( root ).is_balance

#2020.9.26
class ResultType():
    def __init__(self, depth, is_balance):
        self.depth = depth
        self.is_balance = is_balance

class Solution(object):


    def helper(self, root):
        if root == None:
            return ResultType(1, True)

        left_result = self.helper(root.left)
        right_result = self.helper(root.right)

        is_balance = True
        if abs(left_result.depth - right_result.depth) > 1:
            is_balance = False

        if left_result.is_balance and right_result.is_balance and is_balance:
            is_balance = True
        else:
            is_balance = False


        return ResultType(max(left_result.depth, right_result.depth) + 1, is_balance)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.helper(root)


        return res.is_balance


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

    TreeNode1 = TreeNode(1)
    TreeNode2 = TreeNode(2)
    TreeNode3 = TreeNode(3)
    TreeNode4 = TreeNode(4)
    TreeNode5 = TreeNode(5)
    TreeNode6 = TreeNode(6)
    TreeNode7 = TreeNode(7)
    TreeNode8 = TreeNode(8)

    TreeNode1.left = TreeNode2
    TreeNode1.right = TreeNode3
    TreeNode2.left = TreeNode4
    TreeNode2.right = TreeNode5
    TreeNode4.left = TreeNode7
    TreeNode3.right = TreeNode6
    TreeNode6.right = TreeNode8

    print(Solution().isBalanced(TreeNode1))

