class CQueue(object):

    def __init__(self):
        self.stack1 = [] #增加
        self.stack2 = [] #减少


    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2.pop()
        else:
            return -1






if __name__ == '__main__':


    obj = CQueue()
    param_2 = obj.deleteHead()
    print(param_2)
    obj.appendTail(5)
    obj.appendTail(2)

    #obj.appendTail(2)

    # obj.appendTail(2)
    # obj.appendTail(3)
    # obj.appendTail(4)

    param_2 = obj.deleteHead()
    print(param_2)
    param_2 = obj.deleteHead()
    print(param_2)
    # param_2 = obj.deleteHead()
    # print(param_2)
    # param_2 = obj.deleteHead()
    # print(param_2)

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()