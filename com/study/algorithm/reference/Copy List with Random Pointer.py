class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution(object):
    def copyRandomList(self, head):
        if head == None:
            return head

        dummy = Node(0)
        cur = dummy
        dummy.next = cur
        data = {}


        while head != None:
            if data.get(head, None) == None:
                data[head] = Node(head.val)

            cur.next = data[head] #new node



            if head.random != None:
                if data.get(head.random, None) == None:
                    data[head.random] = Node(head.random.val)

                cur.next.random = data[head.random]

            cur = cur.next
            head = head.next

        return dummy.next



if __name__ == '__main__':
    Node3_1 = Node(3)
    Node3_2 = Node(3)
    Node3_3 = Node(3)

    Node3_1.next = Node3_2
    Node3_1.random = None

    Node3_2.next = Node3_3
    Node3_2.random = Node3_1

    Node3_3.next = None
    Node3_3.random = None

    print( Solution().copyRandomList(Node3_1) )

