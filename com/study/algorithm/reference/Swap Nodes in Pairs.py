class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_odd = ListNode(0)
        pre_odd = dummy_odd

        dummy_even = ListNode(0)
        pre_even = dummy_even


        i = 0
        while head:
            if i % 2 == 0:
                pre_odd.next = head
                pre_odd = pre_odd.next

            else:
                pre_even.next = head
                pre_even = pre_even.next
            head = head.next
            i += 1

        pre_odd.next = None
        pre_even.next = None

        odd = dummy_odd.next
        even = dummy_even.next

        dummy = ListNode(0)
        pre = dummy

        i = 1
        while odd and even:
            if i % 2 == 0:
                pre.next = odd
                odd = odd.next
            else:
                pre.next = even
                even = even.next
            pre = pre.next
            i += 1

        if odd:
            pre.next = odd
        if even:
            pre.next = even

        return dummy.next


if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3 = ListNode(3)
    ListNode4 = ListNode(4)

    ListNode1.next = ListNode2
    ListNode2.next = ListNode3
    ListNode3.next = ListNode4

    print(Solution().swapPairs(ListNode1))