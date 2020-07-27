class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#priority queue
#divide conquer
#merge list two by two
class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = head = ListNode()

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1 != None:
            head.next = l1
        else:
            head.next = l2

        return dummy.next


    def mergeHelper(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = int( ( start + end ) / 2)
        left = self.mergeHelper(lists, start, mid)
        right = self.mergeHelper(lists, mid + 1, end)
        return self.mergeTwoLists(left, right)


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if len(lists) == 0:
            return None
        result = self.mergeHelper(lists, 0, len(lists)-1)

        return result


if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode4 = ListNode(4)

    ListNode1.next = ListNode2
    ListNode2.next = ListNode4

    ListNode1_1 = ListNode(1)
    ListNode3 = ListNode(3)
    ListNode4 = ListNode(4)
    ListNode1_1.next = ListNode3
    ListNode3.next = ListNode4

    lists = [ListNode1,ListNode1_1 ]

    print(Solution().mergeKLists(lists))