# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while head!= None:
            if head.val == val:
                pre.next = head.next
                break

            pre = head
            head = head.next

        return dummy.next

if __name__ == '__main__':
    ListNode4 = ListNode(4)
    ListNode5 = ListNode(5)
    ListNode1 = ListNode(1)
    ListNode9 = ListNode(9)

    ListNode4.next = ListNode5
    ListNode5.next = ListNode1
    ListNode1.next = ListNode9

    print( Solution().deleteNode(ListNode4, 9) )


