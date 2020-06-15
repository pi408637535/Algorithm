
class Node():
    def __init__(self, val=None, next=None):
        self._val = val
        self.next = next
    def travel(self):
        while self != None:
            if self._val != None:
                print(self._val)
            self = self.next

if __name__ == '__main__':
    head = Node()
    one = Node(54)
    two = Node(26)

    head.next = one
    one.next = two

    head.travel()
