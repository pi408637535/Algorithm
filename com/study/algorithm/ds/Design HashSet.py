class LinkNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 20000
        self.datas = [None] * self.capacity

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = key % self.capacity
        if not self.datas[hash_key]:
            node = LinkNode(key)
            self.datas[hash_key] = node
        else:
            cur = self.datas[hash_key]
            if cur.val == key:
                return
            else:
                while cur.next:
                    if cur.next.val == key:
                        break
                    else:
                        return

                    cur = cur.next

                node = LinkNode(key)
                cur.next = node





    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = key % self.capacity
        if self.datas[hash_key]:
            cur = self.datas[hash_key]
            if cur.val == key:
                self.datas[hash_key] = cur.next
            else:
                while cur.next:
                    if cur.next.val == key:
                        cur.next = cur.next.next
                        return

                    cur = cur.next


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash_key = key % self.capacity
        if not self.datas[hash_key]:
            return False

        else:
            cur = self.datas[hash_key]
            while cur:
                if cur.val == key:
                    return True
                cur = cur.next

            return False