class Node():
    def __init__(self, value=-1, key = -1, pre = None, next = None):
        self.value = value
        self.key = key
        self.pre = pre
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cur_num = 0
        self.data_map = {}
        self.dummy = Node()
        self.tail = Node()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        #有则返回+调序， 无则-1
        if self.data_map.get(key) == None:
            return -1
        else:

            node = self.data_map[key]
            if not node is self.tail: #节点在中间
                node.pre.next = node.next
                node.next.pre = node.pre


                self.tail.next = node
                node.next = None
                node.pre = self.tail

                self.tail = node




            return self.data_map[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if self.data_map.get(key) != None:

            self.data_map.get(key).value = value

            if not self.data_map.get(key) is self.tail:
                node = self.data_map[key]
                node.pre.next = node.next
                node.next.pre = node.pre

                self.tail.next = node
                node.next = None
                node.pre = self.tail

                self.tail = node

        else:
            if self.cur_num + 1 > self.capacity:
                first_node = self.dummy.next
                del self.data_map[first_node.key]
                self.capacity -= 1
                self.dummy.next = first_node.next

            node = Node(value, key)
            self.data_map[key] = node

            if self.cur_num == 0:

                #self.dummy 解决第一个节点被删问题
                self.dummy.next  = node
                node.pre = self.dummy
                self.tail = node

            else:
                node = Node(value, key)
                self.data_map[key] = node

                self.tail.next = node
                node.pre = self.tail
                self.tail = node

            self.cur_num += 1



if __name__ == '__main__':
    '''
    cache= LRUCache(1)
    cache.put(2, 1)
    print(cache.get(2))
    cache.put(3,2)
    cache.get(2)
    cache.get(3)
    '''

    '''
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)

    cache.get(2)
    cache.put(1,1)
    cache.put(4,1)
    cache.get(2)
    '''

    cache = LRUCache(2)

    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print(cache.get(1))
    print(cache.get(2))

