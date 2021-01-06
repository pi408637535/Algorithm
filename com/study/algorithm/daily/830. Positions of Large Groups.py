class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        res = []
        stack = []
        for index, ele in enumerate(s):
            if not stack: #stack is empty
                stack.append(ele)
            else:
                if stack[-1] == ele:
                    stack.append(ele)
                else:
                    if len(stack) >= 3:
                        res.append([index - len(stack), index - 1])
                    stack = []
                    stack.append(ele)
        if len(stack) >= 3:
            res.append([index - len(stack)+1, index])
        return res

class Solution(object):
    def largeGroupPositions(self, s):

        class Stack():
            def __init__(self):
                self.data = []
            def length(self):
                return len(self.data)
            def push(self, ele):
                if not self.data:
                    self.data.append(ele)
                    return 1
                else:
                    if self.data[-1] != ele:
                        self.data = []
                        self.data.append(ele)
                        return 1
                    else:
                        self.data.append(ele)
                        return len(self.data)

        stack = Stack()
        res = []
        for index, ele in enumerate(s):
            num = stack.push(ele)
            if num == 3:
                res.append([index - num+1, index])
            if num > 3:
                res.pop()
                res.append([index - num+1, index])
        return res


class Solution:
    def largeGroupPositions(self, s):
        res = []
        n, num = len(s), 1

        for i in range(n):
            if i == n - 1  or s[i] != s[i+1]:
                if num >= 3:
                    res.append([i - num + 1, i])
                num = 1
            else:
                num += 1

        return res


if __name__ == '__main__':
    s = "abbxxxxzzy"
    # s = "aaa"
    # s = "aeeeeeeaabbbcd"
    s = "abcdddeeeeaabbbcd"
    print(Solution().largeGroupPositions(s))