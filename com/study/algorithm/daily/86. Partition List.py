# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummyA = ListNode(0)
        dummyB = ListNode(0)
        headA = dummyA
        headB = dummyB

        while head:
            if head.val < x:
                headA.next = head
                headA = headA.next
            else:
                headB.next = head
                headB = headB.next
            head = head.next

        headA.next = dummyB.next
        return dummyA.next

if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode4 = ListNode(4)
    ListNode3 = ListNode(3)
    ListNode2_1 = ListNode(2)
    ListNode5 = ListNode(5)
    ListNode2_2 = ListNode(2)

    ListNode1.next = ListNode4
    ListNode4.next = ListNode3
    ListNode3.next = ListNode2_1
    ListNode2_1.next = ListNode5
    ListNode5.next = ListNode2_2

    res = Solution().partition(ListNode1)
    res


