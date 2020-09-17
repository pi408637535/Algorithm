class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#priority queue
#divide conquer
#merge list two by two
class Solution(object):

    def merge(self, left, right):
        dummy = ListNode(0)
        pre = dummy

        left = left[0]
        right = right[0]

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

        return [dummy.next]

    def mergeSort(self, lists):
        if len(lists) < 2:
            return lists



        mid = len(lists) // 2

        left = lists[0:mid]
        right = lists[mid:]

        return self.merge(self.mergeSort(left), self.mergeSort(right))


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        res = self.mergeSort(lists)
        return res[0]

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