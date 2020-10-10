class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_dummy = ListNode(0)
        even_dummy = ListNode(0)

        odd_pre = odd_dummy
        even_pre = even_dummy

        i = 1
        while head:
            if i % 2 ==0:
                even_pre.next = head
                even_pre = even_pre.next
            else:
                odd_pre.next = head
                odd_pre = odd_pre.next
            head = head.next
            i += 1

        even_pre.next = None
        odd_pre.next = None

        dummy = ListNode(0)
        pre = dummy

        even = even_dummy.next
        while even:
            pre.next = even
            even = even.next
            pre = pre.next

        odd = odd_dummy.next
        while odd:
            pre.next = odd
            odd = odd.next
            pre = pre.next

        return dummy.next

if __name__ == '__main__':
    pass