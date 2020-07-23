class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def hasCycle(self, head):
        if head.next == None:
            return False

        fast = head.next.next
        slow = head

        while fast != None:
            if fast.next != None:
                if fast.val == slow.val:
                    return True

                fast = fast.next.next
                slow = slow



            else:
                return False

        return False



if __name__ == '__main__':
    pass