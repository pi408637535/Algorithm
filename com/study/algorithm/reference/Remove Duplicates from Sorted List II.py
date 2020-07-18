class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head

        pre = dummy

        while head != None:
            if head.next != None and head.next.val == head.val:
                val = head.val
                while head != None and head.val == val:
                    head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next

        return dummy.next




if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3_1 = ListNode(3)
    ListNode3_2 = ListNode(3)
    ListNode4_1 = ListNode(4)
    ListNode4_2 = ListNode(4)
    ListNode5 = ListNode(5)

    ListNode1.next = ListNode2
    ListNode2.next = ListNode3_1
    ListNode3_1.next = ListNode3_2
    ListNode3_2.next = ListNode4_1
    ListNode4_1.next = ListNode4_2
    ListNode4_2.next = ListNode5

    print(Solution().deleteDuplicates(ListNode1))


