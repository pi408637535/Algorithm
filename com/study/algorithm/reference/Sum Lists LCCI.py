class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre = dummy

        flag = 0

        while l1 and l2:
            value = l1.val + l2.val
            value += flag
            value = value - 10 * flag

            node = ListNode(value % 10)
            node.next = pre.next
            pre.next = node
            pre = pre.next
            flag = (l1.val + l2.val) // 10

            l1 = l1.next
            l2 = l2.next

        pre.next = l1 or l2
        node = pre.next

        while flag and node:

            if node.val == 9:
                node.val = 0
            else:
                node.val += 1
                flag = 0

            node = node.next
            pre = pre.next

        pre.next = ListNode(1) if flag else l1 or l2

        return dummy.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return ListNode(0)

        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(0)
        pre = dummy

        over_bit = 0
        while l1 and l2:
            if l1.val + l2.val + over_bit  >= 10:
                flag = 1
            else:
                flag = 0

            val = l1.val + l2.val + over_bit - 10 * flag
            node = ListNode(val)
            pre.next = node
            pre = pre.next

            l1 = l1.next
            l2 = l2.next
            over_bit = flag

        pre.next = l1 or l2

        if pre.val == 10:
            flag = 1

        while flag and pre.next:
            if pre.next.val >= 9:
                flag = 1
            else:
                pre.next.val = pre.next.val + 1
                flag = 0
            pre.next.val = pre.next.val + flag - 10 * flag
            pre = pre.next

        if flag:

            if pre.val == 10:
                pre.val = 0

            pre.next = ListNode(1)

        return dummy.next

if __name__ == '__main__':
    '''
    ListNode7 = ListNode(7)
    ListNode1 = ListNode(1)
    ListNode6 = ListNode(6)

    ListNode5 = ListNode(5)
    ListNode9 = ListNode(9)
    ListNode2 = ListNode(2)

    ListNode7.next = ListNode1
    ListNode1.next = ListNode6

    ListNode5.next = ListNode9
    ListNode9.next = ListNode2

    print(Solution().addTwoNumbers(ListNode7, ListNode5))

    ListNode0 = ListNode(0)

    ListNode7 = ListNode(7)
    ListNode3 = ListNode(3)
    ListNode7.next = ListNode3
    print(Solution().addTwoNumbers(ListNode0, ListNode7))

    ListNode1 = ListNode(1)

    ListNode9_1 = ListNode(9)
    ListNode9_2 = ListNode(9)
    ListNode9_1.next = ListNode9_2
    print(Solution().addTwoNumbers(ListNode1, ListNode9_1))


    ListNode0 = ListNode(0)

    ListNode1 = ListNode(1)
    ListNode8 = ListNode(8)
    ListNode1.next = ListNode8
    '''
    ListNode1 = ListNode(1)

    ListNode9 = ListNode(9)
    ListNode8 = ListNode(8)
    ListNode9.next = ListNode8
    print(Solution().addTwoNumbers(ListNode1, ListNode9))






