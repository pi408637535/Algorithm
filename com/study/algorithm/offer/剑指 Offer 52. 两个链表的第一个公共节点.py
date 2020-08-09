class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dummyA = ListNode(0)
        pre = dummyA.next
        while headA != None:
            temp = headA.next
            dummyA.next = headA
            headA.next = pre

            pre = headA
            headA = temp

        dummyB = ListNode(0)
        pre = dummyB.next
        while dummyB != None:
            temp = headB.next
            dummyB.next = headB
            headB.next = pre

            pre = headB
            headB = temp

        headA = dummyA.next
        headB = dummyB.next

        pre = None
        while headA.val == headB.val:
            pre = headA

            headA = headA.next
            headB = headB.next

        return pre



if __name__ == '__main__':
