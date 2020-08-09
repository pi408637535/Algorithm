class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        data = []
        while head != None:
            data.append(head.val)

        return data[::-1]

if __name__ == '__main__':
    pass