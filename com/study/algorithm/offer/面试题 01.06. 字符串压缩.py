
class LinkList():
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        dummy = LinkList(0, 0)
        pre = dummy
        i = 0
        if len(S):
            node = LinkList(S[0], 1)
            pre.next = node
            pre = pre.next
            i += 1


        for ele in S[1:]:
            if pre.key != ele:
                node = LinkList(ele, 1)
                pre.next = node
                pre = pre.next
                i += 1
            else:
                pre.value += 1

        if i != 0 and i * 2 < len(S):
            head = dummy.next
            new_s = ""
            while head:
                new_s += str(head.key) + str(head.value)
                head = head.next

            return new_s
        else:
            return S

import collections
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        queue = collections.deque()

        last_ele = None
        for ele in S:
            if not last_ele or ele != last_ele:
                queue.append({ele:1})
                last_ele = ele
            else:
                queue[-1][ele] += 1

        if len(queue) * 2 < len(S):
            new_s = ""
            while queue:
                temp = queue.popleft()
                new_s += str(list(temp.keys())[0])+ str(list(temp.values())[0])
            return new_s
        else:
            return S


class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        i,j = 0,0
        new_s = ""
        length = len(S)
        while i < length:
            if S[i] == S[j]:
                i += 1
            else:
                new_s += S[j] + str(i - j)
                j = i
        if j != i:
            new_s += S[j] + str(i - j)

        if len(new_s) < len(S):
            return new_s
        else:
            return S






if __name__ == '__main__':
    s = "aabcccccaaa"
    #s = "abbccd"
    #s = 'a'
    #s = 'ccc'
    print(Solution().compressString(s))




