class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow = head
        fast = head.next.next

        while fast != None:
            if not fast or not fast.next:
                return False

            if fast.val == slow.val:
                return True

            fast = fast.next.next
            slow = slow.next

        return False


class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while True:
            if not fast or not fast.next:
                return False

            if fast.val == slow.val:
                return True

            fast = fast.next.next
            slow = slow.next



if __name__ == '__main__':
    ListNode3 = ListNode(3)
    ListNode2 = ListNode(2)
    ListNode0 = ListNode(0)
    ListNode4 = ListNode(4)

    ListNode3.next = ListNode2
    ListNode2.next = ListNode0
    ListNode0.next = ListNode4

    ListNode4.next = ListNode2

    print( Solution().hasCycle(ListNode3) )



