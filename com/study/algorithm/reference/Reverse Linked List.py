class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()

        pre = dummy
        cur = head

        while head != None:
            temp = pre.next
            pre.next = head
            head = head.next
            pre.next.next = temp
            if cur == head:
                cur.next = None

        return dummy.next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head

        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp


        return pre


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        pre = dummy

        while head != None:
            temp = pre.next
            pre.next = head
            head = head.next
            pre.next.next = temp


        return pre.next


if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3 = ListNode(3)
    ListNode4 = ListNode(4)
    ListNode5 = ListNode(5)

    ListNode1.next = ListNode2
    ListNode2.next = ListNode3
    ListNode3.next = ListNode4
    ListNode4.next = ListNode5

    print(Solution().reverseList(ListNode1))