class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = head = ListNode()

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1 != None:
            head.next = l1
        else:
            head.next = l2

        return dummy.next

#2020.9.29
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre = dummy

        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next

        if l1:
            pre.next = l1
        if l2:
            pre.next = l2

        return dummy.next


if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode4 = ListNode(4)

    ListNode1.next = ListNode2
    ListNode2.next = ListNode4

    ListNode1_1 = ListNode(1)
    ListNode3 = ListNode(3)
    ListNode4 = ListNode(4)
    ListNode1_1.next = ListNode3
    ListNode3.next = ListNode4

    print(Solution().mergeTwoLists(ListNode1, ListNode1_1))