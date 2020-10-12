# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast,slow = head,head
        pre = None
        while fast and fast.next:
            slow_next = slow.next
            fast = fast.next.next
            slow.next = pre
            pre = slow
            slow = slow_next

        if fast:
            fast = slow.next
            slow = pre
        else:
            fast = slow
            slow = pre


        while fast and slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next

        return True


if __name__ == '__main__':
    '''
    ListNode1_1 = ListNode(1)
    ListNode2_1 = ListNode(2)
    ListNode2_2 = ListNode(2)
    ListNode1_2 = ListNode(1)

    ListNode1_1.next = ListNode2_1
    ListNode2_1.next = ListNode2_2
    ListNode2_2.next = ListNode1_2
    '''


    '''
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3 = ListNode(3)

    ListNode1.next = ListNode2
    ListNode2.next = ListNode3
    '''

    ListNode1_1 = ListNode(1)
    ListNode2_1 = ListNode(2)
    ListNode2_2 = ListNode(2)
    ListNode2_3 = ListNode(2)
    ListNode1_2 = ListNode(1)

    ListNode1_1.next = ListNode2_1
    ListNode2_1.next = ListNode2_2
    ListNode2_2.next = ListNode2_3
    ListNode2_3.next = ListNode1_2
    print(Solution().isPalindrome(ListNode1_1))
