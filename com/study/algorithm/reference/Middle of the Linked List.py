class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head.next == None:
            return head


        fast_node = head.next.next
        slow_node = head

        while fast_node != None:
            if fast_node.next == None:
                break
            slow_node = slow_node.next
            fast_node = fast_node.next.next


        return slow_node.next



if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3 = ListNode(3)
    ListNode4 = ListNode(4)
    ListNode5 = ListNode(5)
    ListNode6 = ListNode(6)

    ListNode1.next = ListNode2
    ListNode2.next = ListNode3
    ListNode3.next = ListNode4
    ListNode4.next = ListNode5
    ListNode5.next = ListNode6

    print(Solution().middleNode(ListNode1))