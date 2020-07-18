class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def __init__(self):
        self.val_set = set()
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        pre = None
        while head != None:
            if head.val not in self.val_set:
                self.val_set.add(head.val)
                pre = head
                head = head.next
            else:
                pre.next = head.next
                head = head.next
        return result



if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode1_1 = ListNode(1)
    ListNode2 = ListNode(2)

    ListNode1.next = ListNode1_1
    ListNode1_1.next = ListNode2

    print( Solution().deleteDuplicates(ListNode1) )

