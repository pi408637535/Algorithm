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
        list_one_length = 0
        dummyA = ListNode(0)
        dummyA.next = headA

        while headA != None:
            list_one_length += 1
            headA = headA.next



        list_two_length = 0
        dummyB = ListNode(0)
        dummyB.next = headB

        while dummyB != None:
            list_two_length += 1
            headB = headB.next

        num = list_one_length - list_two_length
        if num > 0:
            fast_node = dummyA.next
            while num > 0:
                fast_node = fast_node.next
                num -= 1
            slow_node = dummyB.next
        else:
            fast_node = dummyB.next
            while num < 0:
                fast_node = fast_node.next
                num += 1
            slow_node = dummyA.next

        while fast_node != None and slow_node != None:
            if fast_node == slow_node:
                return fast_node
            fast_node = fast_node.next
            slow_node = slow_node.next

        return None


if __name__ == '__main__':
    pass

