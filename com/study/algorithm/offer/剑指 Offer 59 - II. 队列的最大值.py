import heapq

class MaxQueue(object):

    def __init__(self):
        self.heap = []
        self.queue = [0 for i in range(100)]
        self.pre = 0
        self.tail = 0
        self.num = 100

    def max_value(self):
        """
        :rtype: int
        """
        if len(self.heap) == 0:
            return -1
        else:
            return -self.heap[0]


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """


        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.num

        heapq.heappush(self.heap, -value)

    def pop_front(self):
        """
        :rtype: int
        """
        if self.tail == self.pre:
            return -1
        else:
            temp= self.queue[self.pre]
            self.pre = (self.pre + 1) % self.num
            heapq.heappop(self.heap)
            return temp


if __name__ == '__main__':
    obj = MaxQueue()
    param_1 = obj.max_value()
    print(param_1)
    obj.push_back(1)
    obj.push_back(2)
    param_1 = obj.max_value()
    print(param_1)

    param_3 = obj.pop_front()
    print(param_3)
    param_3 = obj.max_value()
    print(param_3)

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()