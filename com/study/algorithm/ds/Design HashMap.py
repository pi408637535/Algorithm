class ListNode():
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 2000
        self.datas = [None] * self.capacity



    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        key = key % self.capacity
        if not self.datas[key]:
            node = ListNode(key, value)
            self.datas[key] = node
        else:
            pre = self.datas[key]

            if pre.key == key:
                pre.val = value
                return


            while pre.next:
                if pre.next.key == key:
                    pre.next.val = value
                    break

            new_node = ListNode(key, value)
            pre.next = new_node

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        key = key % self.capacity
        if not self.datas[key]:
            return -1
        else:
            node = self.datas[key]
            while node:
                if node.key == key:
                    return node.val
                node = node.next
            return -1



    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        key = key % self.capacity
        if self.datas[key]:
            pre = self.datas[key]
            if pre.key == key:
                self.datas[key] = pre.next
                return

            while pre.next:
                if pre.next.key == key:
                    pre.next = pre.next.next
                    break


if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    print(obj.get(3))
    obj.put(2, 1)
    print(obj.get(2))
    obj.remove(2)
    print(obj.get(2))




