# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 13:25
# @Author  : piguanghua
# @FileName: Linked List Cycle II.py
# @Software: PyCharm

# a + b 为总链表数量
# f = 2s , f = s + nb 相遇时情况


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while True:
            if not fast or not fast.next:
                return False

            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break




        #loop
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.val



if __name__ == '__main__':
    ListNode3 = ListNode(3)
    ListNode2 = ListNode(2)
    ListNode0 = ListNode(0)
    ListNode4 = ListNode(4)

    ListNode3.next = ListNode2
    ListNode2.next = ListNode0
    ListNode0.next = ListNode4

    ListNode4.next = ListNode2

    print(Solution().detectCycle(ListNode3))



