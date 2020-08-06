class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = None

        pre = dummy
        i = 1
        last = None
        while head != None:

            if m <= i and i <= n:
                if i == m:
                    pre.next = None
                temp = pre.next
                pre.next = head
                head = head.next
                pre.next.next = temp

                if i == m:
                    last = pre.next

            else:
                pre.next = head
                pre = head
                head = head.next

            i += 1

            if i > n:
                break
        last.next = head

        return dummy.next


class Solution(object):
    #寻找开始，结束节点
    #倒排
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if head == None:
            return None

        dummy = ListNode()
        dummy.next = head

        cur = dummy  # 寻找开始点之前的结点

        i = 1
        while i < m:
            if cur == None:
                return None
            cur = cur.next
            i += 1


        pre = cur
        mNode = cur.next

        #reverse m -> n
        nNode = mNode
        postNode = mNode.next

        i = m
        while i < n:
            if postNode == None:
                return None
            temp = postNode.next
            postNode.next = nNode
            nNode = postNode
            postNode = temp
            i += 1

        #connect m-1->n, m->n+1
        mNode.next = postNode
        pre.next = nNode



        return dummy.next


class Solution(object):
    def reverseBetween(self, head, m, n):

        if head == None:
            return None

        dummy = ListNode()
        dummy.next = head

        pre = dummy
        #i<m
        i = 1
        while i < m:
            if pre == None:
                return None
            pre = pre.next
            i += 1

        # m <= i < n

        cur = pre.next
        mNode = cur
        postNode = cur.next

        i = m
        while i < n:
            if postNode == None:
                return None

            temp = postNode.next
            postNode.next = cur
            cur = postNode
            postNode = temp
            i += 1

        # connect m, n+1
        mNode.next = postNode
        pre.next = cur

        return dummy.next


if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3 = ListNode(3)
    ListNode4 = ListNode(4)
    ListNode5 = ListNode(5)

    ListNode1.next = ListNode2
    ListNode2.next = ListNode3
    ListNode3.next = ListNode4
    ListNode4.next = ListNode5

    m = 2
    n = 5
    print(Solution().reverseBetween(ListNode1, m, n))