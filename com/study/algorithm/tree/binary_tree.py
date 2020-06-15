
class BinaryTree():
    def __init__(self,value,left=None,right=None):
        self._value = value
        self.left = left
        self.right = right

    def __str__(self):
        print("val={0},left={1}, right={2}"
              .format(self._value, self.right, self.right))

if __name__ == '__main__':

    root = BinaryTree(8)
    node = BinaryTree(3)
    root.left = node
    node = BinaryTree(10)
    root.right = node

