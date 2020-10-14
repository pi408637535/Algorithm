# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import collections
class Solution(object):
    def listOfDepth(self, tree):
        """
        :type tree: TreeNode
        :rtype: List[ListNode]
        """
        if not tree:
            return []
        queue = collections.deque()
        queue.append(tree)
        res = []
        while queue:

            dummy = ListNode(0)
            pre = dummy
            for _ in range(len(queue)):
                tree_node = queue.popleft()
                link_node = ListNode(tree_node.val)
                link_node.next = pre.next
                pre.next = link_node
                pre = pre.next

                if tree_node.left:
                    queue.append(tree_node.left)
                if tree_node.right:
                    queue.append(tree_node.right)

            if dummy.next:
                res.append(dummy.next)

        return res


