
class BinaryTree():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        print("val={0},left={1}, right={2}"
              .format(self.value, self.left, self.right))


def recursive_pre(node):
    if node == None:
        return
    else:
        if node.value == 3:
            print("")
        print(node.value)
        recursive_pre(node.left)
        recursive_pre(node.right)


if __name__ == '__main__':

    node1 = BinaryTree(1)
    node2 = BinaryTree(2)
    node3 = BinaryTree(3)
    node4 = BinaryTree(4)
    node5 = BinaryTree(5)
    node6 = BinaryTree(6)
    node7 = BinaryTree(7)

    node1.left = node2
    node1.right = node3

    node2.left = node4

    node3.left = node5
    node3.right = node6

    node6.left = node7

    recursive_pre(node1)







