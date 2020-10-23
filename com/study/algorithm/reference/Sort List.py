class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution(object):

    def getLinkListMiddle(self, head):
        #return middle node
        i = 1
        temp = head
        while head:
            head = head.next
            i += 1

        middle = i // 2
        i = 1
        while temp and i < middle:
            temp = temp.next
            i += 1
        return temp


    def merget(self, left, right):
        dummy = ListNode(0)
        pre = dummy
        while left and right:
            if left.val < right.val:
                pre.next = left
                left = left.next
            else:
                pre.next = right
                right = right.next

            pre = pre.next

        if left:
            pre.next = left
        if right:
            pre.next = right

        return dummy.next


    def mergetSort(self, head):
        if head:
            if not head.next:
                return head

            else:
                middle_node = self.getLinkListMiddle(head)
                right_head = middle_node.next
                middle_node.next = None
                left = head
                right = right_head

                return self.merget( self.mergetSort(left), self.mergetSort(right) )

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = self.mergetSort(head)
        return res



class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        return self._merge_sort(head)

    def _middle_head(self, head):
        fast = head.next
        slow = head
        while  fast and  fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge_sort(self, head):
        if not head:
            return None
        if not head.next:
            return head

        middle_node = self._middle_head(head)
        right = middle_node.next
        left = head
        middle_node.next = None

        return self._merge(self._merge_sort(left), self._merge_sort(right))

    def _merge(self, left, right):
        dummy = ListNode(0)
        pre = dummy
        while left and right:
            if left.val < right.val:
                pre.next = left
                left = left.next
            else:
                pre.next = right
                right = right.next
            pre = pre.next

        if left:
            pre.next = left
        if right:
            pre.next = right

        return  dummy.next

if __name__ == '__main__':
    ListNode4 = ListNode(4)
    ListNode2 = ListNode(2)
    ListNode1 = ListNode(1)
    ListNode3 = ListNode(3)
    ListNode5 = ListNode(5)

    ListNode4.next = ListNode2
    ListNode2.next = ListNode1
    ListNode1.next = ListNode3
    ListNode3.next = ListNode5

    print(Solution().sortList(ListNode4))

