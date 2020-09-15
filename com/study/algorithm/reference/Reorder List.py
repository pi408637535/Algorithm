class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def __middleLinkList(self, head):
        fast = head.next
        slow = head
        while  fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def __reverseLinkList(self, head):
        dummy = ListNode(0)
        pre = dummy

        while head:
            temp = head.next
            head.next = pre.next
            pre.next = head
            head = temp

        return dummy.next

    def __conbination(self, left, right):
        dummy = ListNode(0)

        pre = dummy
        pre.next = left

        while left and right:
            temp_a = left.next
            temp_b = right.next

            left.next = right
            right.next = temp_a

            left = temp_a
            right = temp_b

            pre = pre.next.next

        if right:
            pre.next = right

        return dummy.next


    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if head == None:
            return None

        middle_node = self.__middleLinkList(head)
        right = middle_node.next
        middle_node.next = None
        left = head

        right = self.__reverseLinkList(right)

        root = self.__conbination(left, right)
        return root

if __name__ == '__main__':
    ListNode1 = ListNode(1)
    # ListNode2 = ListNode(2)
    # ListNode3 = ListNode(3)
    # ListNode4 = ListNode(4)
    # ListNode5 = ListNode(5)
    #
    # ListNode1.next = ListNode2
    # ListNode2.next = ListNode3
    # ListNode3.next = ListNode4
    # ListNode4.next = ListNode5
    
    print(Solution().reorderList(ListNode1))

