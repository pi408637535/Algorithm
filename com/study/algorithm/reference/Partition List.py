# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 11:58
# @Author  : piguanghua
# @FileName: Partition List.py
# @Software: PyCharm

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_a = ListNode(0) #lt
        dummy_b = ListNode(0) #equal、gt

        cur_a = dummy_a
        cur_b = dummy_b

        while head:
            if head.val < x:
                cur_a.next = head
                cur_a = cur_a.next
            else:
                cur_b.next = head
                cur_b = cur_b.next

            head = head.next

        cur_a.next = dummy_b.next
        cur_b.next = None

        return dummy_a.next




if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2_2 = ListNode(2)
    ListNode2_1 = ListNode(2)

    ListNode3 = ListNode(3)
    ListNode4 = ListNode(4)
    ListNode5 = ListNode(5)

    ListNode1.next = ListNode4
    ListNode4.next = ListNode3
    ListNode3.next = ListNode2_1
    ListNode2_1.next = ListNode5
    ListNode5.next = ListNode2_2

    print( Solution().partition(ListNode1, 3) )

