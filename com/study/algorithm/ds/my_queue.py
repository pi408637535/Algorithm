
'''
问题:优于循环队列的 空判别
'''

class CirculationQueue(object):
    def __init__(self, max):
        self._front = 0
        self._rear = 0
        self._array = [None] * max
        self._max = max

    def pop(self):
        if self._front == self._rear:
            return -1
        else:
            data = self._array[self._front]
            self._front = (self._front + 1) % self._max
            return data

    def push(self, element):
        if self._full():
            return -1
        else:
            self._array[self._rear] = element
            self._rear = (self._rear + 1) % self._max
            return 0

    def _full(self):
        if (self._rear + 1 ) % self._max == self._front:
            return True
        else:
            return False

    def _empty(self):
        if self._front == self._rear:
            return True
        else:
            return False

    def show_queue(self):
        front = self._front
        if front == self._rear and self._front == 0:
            print()
        else:
            while front != self._rear:
                print(self._array[front])
                front = (front + 1) % self._max

    @property
    def array(self):
        return self._array

if __name__ == '__main__':
    cq = CirculationQueue(13)
    year = 42
    total_money = 0
    month_money = 1000
    rate = 0.0471

    for i in range(year):
        for j in range(12):
            result = cq.push(month_money)
            if result == -1:
                temp_money = cq.pop()
                temp_money = temp_money * (1 + rate) + month_money
                cq.push(temp_money)

    data = cq.pop()
    while data != -1:
        total_money += data
        data = cq.pop()
    print(total_money)


