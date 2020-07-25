
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):


    def rotateRight(self, head, k):

        if head == None or head.next == None or k == 0:
            return head

        length = 1
        real_head = head
        while head.next != None:
            head = head.next
            length += 1

        #circle
        head.next = real_head

        tail = head.next
        for i in range(length - k % length - 1):
            tail = tail.next

        head = tail.next
        tail.next = None

        return head


if __name__ == '__main__':

    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3 = ListNode(3)

    ListNode4 = ListNode(4)
    ListNode5 = ListNode(5)
   # ListNode6 = ListNode(6)

    ListNode1.next = ListNode2
    ListNode2.next = ListNode3
    ListNode3.next = ListNode4
    ListNode4.next = ListNode5
    #ListNode5.next = ListNode6

    print(Solution().rotateRight(ListNode1, k = 2))