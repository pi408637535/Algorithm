
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        pre = dummy

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next

            pre.next = temp
            pre = temp



        if l1 != None:
            pre.next = l1
        elif l2 != None:
            pre.next = l2

        return dummy.next

if __name__ == '__main__':
    ListNode1_1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode4_1 = ListNode(4)
    ListNode1_1.next = ListNode2
    ListNode2.next = ListNode4_1

    ListNode1_2 = ListNode(1)
    ListNode3 = ListNode(3)
    ListNode4_2 = ListNode(4)
    ListNode1_2.next = ListNode3
    ListNode3.next = ListNode4_2

    print( Solution().mergeTwoLists(ListNode1_1, ListNode1_2) )

