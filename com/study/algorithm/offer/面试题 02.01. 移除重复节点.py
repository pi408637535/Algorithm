# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre = dummy
        data_set = set()

        while head:
            if not pre.next or head.val not in data_set:
                pre.next = head
                pre = pre.next
                data_set.add(head.val)

            head = head.next
        pre.next = head

        return dummy.next


if __name__ == '__main__':
    ListNode1_1 = ListNode(1)
    ListNode1_2 = ListNode(2)
    ListNode1_3 = ListNode(3)
    ListNode2_1 = ListNode(2)
    ListNode3 = ListNode(3)
    ListNode2_2 = ListNode(2)
    ListNode1_4 = ListNode(1)

    ListNode1_1.next = ListNode1_2
    ListNode1_2.next = ListNode1_3
    ListNode1_3.next = ListNode2_1
    ListNode2_1.next = ListNode3
    ListNode3.next = ListNode2_2
    ListNode2_2.next = ListNode1_4
    print(Solution().removeDuplicateNodes(ListNode1_1))





