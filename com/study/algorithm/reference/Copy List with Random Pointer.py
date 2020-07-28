class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        hashmap = {}
        dummy = Node(0)
        dummy.next = head

        if head == None:
            return head

        pre = dummy

        while head != None:
            if hashmap.get(head, None) != None:
                new_node = hashmap[head]
            else:
                new_node = Node(head.val)
                hashmap[head] = new_node

            pre.next = new_node

            if head.random != None:
                if hashmap.get(head.random, None) != None:
                    new_node.random = hashmap.get(head.random)
                else:
                    new_node.random = Node(head.random.val)
                    hashmap[head.random] = new_node.random

            pre = new_node
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

