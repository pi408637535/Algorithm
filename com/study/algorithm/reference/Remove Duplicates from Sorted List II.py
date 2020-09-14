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
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = head

        while cur:

            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
                #pre = pre.next
            else:

                pre = pre.next
                cur = cur.next
        pre.next = cur
        return dummy.next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = head

        while cur:

            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
                # cur = cur.next
                #pre = pre.next
            else:

                pre = pre.next
                cur = cur.next
        pre.next = cur
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


