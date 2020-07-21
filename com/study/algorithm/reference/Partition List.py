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
        left_dummy = ListNode()
        right_dummy = ListNode()

        left_post = left_dummy
        right_post = right_dummy

        while head != None:
            if head.val < x:
                left_post.next = head
                left_post = head
            else:
                right_post.next = head
                right_post = head

            head = head.next
        right_post.next = None # head跳出循环时，有可能不是在最后一个节点跳出的，所以需要注意
        if left_dummy.next == None:
            return right_dummy.next
        else:
            left_post.next = right_dummy.next
            return left_dummy.next



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

