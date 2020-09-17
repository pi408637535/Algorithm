# class LinkNode():
#     def __init__(self,key,value,pre=None, next=None):
#         self.val = value
#         self.key = key
#         self.pre = pre
#         self.next = next
#
# class LRUCache(object):
#
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.dummy = LinkNode(0,0)
#         self.dic = {}
#         self.num = 0
#
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if not self.dic.get(key):
#             return -1
#         else:
#             val = self.dic[key].val
#
#             cur = self.dic[key]
#             pre = cur.pre
#
#             if not cur.next: #last
#                 return val
#             else: #middle
#                 pre.next = cur.next
#                 cur.next.pre = pre
#
#                 temp = pre.next
#                 while temp:
#                     temp = temp.next
#                     pre = pre.next
#                 node = LinkNode(key, val)
#                 node.pre = pre
#                 pre.next = node
#                 self.dic[key] = node
#                 return val
#
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#
#         if self.num == self.capacity:
#             if not self.dic.get(key):
#                 del self.dic[ self.dummy.next.key ]
#                 self.num -= 1
#             else:
#                 if not self.dummy.next.next:
#                     self.dummy.next = None
#                 else:
#                     self.dummy.next = self.dummy.next.next
#                     self.dummy.next.pre = self.dummy
#
#
#
#         #put分两种：1.新节点 2.存在
#         if not self.dic.get(key): # new node
#
#             pre = self.dummy
#             cur = pre.next
#             while cur:
#                 cur = cur.next
#                 pre = pre.next
#             node = LinkNode(key, value)
#             pre.next = node
#             node.pre = pre
#             self.dic[key] = node
#             self.num += 1
#
#         else:
#             #middle or last
#             cur = self.dic[key]
#             if not cur.next: #last
#                 cur.val = value
#             else: #middle
#                 cur.pre.next = cur.next
#                 cur.next.pre = cur.pre
#
#                 pre = cur.pre
#                 while pre.next:
#                     pre = pre.next
#                 node = LinkNode(key,value)
#                 pre.next = node
#                 node.pre = node
#                 self.dic[key] = node


class LinkNode():
    def __init__(self, key,val, pre=None, next=None):
        self.val = val
        self.key = key
        self.next = next
        self.pre = pre

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = LinkNode(0,0)
        self.tail = LinkNode(0,0)

        self.head.next = self.tail
        self.tail.pre = self.head

    def moveNodeToLast(self, node):
        last_node = self.tail.pre
        if not node == last_node:
            node.pre.next = node.next
            node.next.pre = node.pre

            last_node.next = node
            node.next = self.tail
            node.pre = last_node
            self.tail.pre = node


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not self.dic.get(key):  # new node
            return -1
        else:
            node = self.dic.get(key)
            self.moveNodeToLast(node)
            return node.val



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # new node or old node

        if not self.dic.get(key): #new node
            if len(self.dic) == self.capacity:
                del self.dic[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.pre = self.head

            node = LinkNode(key, value)
            self.dic[key] = node

            self.tail.pre.next = node
            node.pre = self.tail.pre
            node.next = self.tail
            self.tail.pre = node
        else:
            node = self.dic.get(key)
            node.val = value
            self.moveNodeToLast(node)



if __name__ == '__main__':
    # obj = LRUCache(2)
    # print(obj.get(2))
    # obj.put(2, 6)
    # print(obj.get(1))
    # print(obj.put(1, 5))
    # print(obj.put(1, 2))
    # print(obj.get(1))
    # print(obj.get(2))

    # obj = LRUCache(2)
    # obj.put(2,1)
    # obj.put(1,1)
    # obj.put(2,3)
    # obj.put(4,1)
    # print(obj.get(1))
    # print(obj.get(2))

    # obj = LRUCache(2)
    # obj.put(2,1)
    # obj.put(1,1)
    # print(obj.get(2))
    # obj.put(4,1)
    # print(obj.get(1))
    # print(obj.get(2))

    obj = LRUCache(3)
    obj.put(1,1)
    obj.put(2,2)
    obj.put(3,3)
    obj.put(4,4)
    print(obj.get(4))
    print(obj.get(3))
    print(obj.get(2))
    print(obj.get(1))
    obj.put(5,5)
    print(obj.get(1))
    print(obj.get(2))
    print(obj.get(3))
    print(obj.get(4))
    print(obj.get(5))

    # obj = LRUCache(1)
    # obj.put(2,1)
    # print(obj.get(2))
    # obj.put(3,2)
    # print(obj.get(2))
    # print(obj.get(3))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)