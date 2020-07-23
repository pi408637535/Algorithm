class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """


        dummy = ListNode()
        dummy.next = head



        pre = dummy
        slow_node = head
        for i in range(n):
            head = head.next
        fast_node = head

        
        while fast_node != None:
            fast_node = fast_node.next
            pre = pre.next
            slow_node = slow_node.next

        pre.next = slow_node.next

        return dummy.next
            
        
if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3 = ListNode(3)
    ListNode4 = ListNode(4)
    ListNode5 = ListNode(5)
    #ListNode6 = ListNode(6)

    #ListNode1.next = ListNode2
    #ListNode2.next = ListNode3
    #ListNode3.next = ListNode4
    #ListNode4.next = ListNode5
    #ListNode5.next = ListNode6
    
    print(Solution().removeNthFromEnd(ListNode1, 1))