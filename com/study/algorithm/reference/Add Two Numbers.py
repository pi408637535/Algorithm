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
        dummy = ListNode()
        pre = dummy

        flag = 0 #represent pre statue
        while l1 and l2:
            gt_ten = 1 if l1.val + l2.val + flag >= 10 else 0
            value = l1.val + l2.val + flag - 10 * gt_ten

            if l1.val + l2.val+ flag >= 10:
                flag = 1
            else:
                flag = 0

            l1.val = value
            pre.next = l1
            l1 = l1.next
            l2 = l2.next
            pre = pre.next

        pre.next = l1 or l2
        cur = pre.next
        while flag and cur:
            if cur.val == 9:
                cur.val = 0
                flag = 1
            else:
                cur.val += 1
                flag = 0
            cur = cur.next
            pre = pre.next

        if flag:
            pre.next = ListNode(1)

        return dummy.next

if __name__ == '__main__':
    '''
    ListNode2 = ListNode(2)
    ListNode4_1 = ListNode(4)
    ListNode3 = ListNode(3)

    ListNode5 = ListNode(5)
    ListNode6 = ListNode(6)
    ListNode4_2 = ListNode(4)

    ListNode2.next = ListNode4_1
    ListNode4_1.next = ListNode3

    ListNode5.next = ListNode6
    ListNode6.next = ListNode4_2
    '''

    ListNode3 = ListNode(3)
    ListNode7 = ListNode(7)

    ListNode9 = ListNode(9)
    ListNode2 = ListNode(2)

    ListNode3.next = ListNode7
    ListNode9.next = ListNode2

    print(Solution().addTwoNumbers(ListNode3, ListNode9))

    res = 'None' or []
    print(res)



