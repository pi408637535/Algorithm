class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#priority queue
#divide conquer
#merge list two by two
class Solution(object):

    def conpare(self, left, right):
        if left == None:
            return 1
        elif right == None:
            return -1
        return left.val - right.val


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

if __name__ == '__main__':
