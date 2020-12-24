import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.defaultdict()
        for ele in s:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1

        for index,ele in enumerate(dic):
            if dic[ele] == 1:
                return index

        return -1


class Solution:
    def firstUniqChar(self, s: str):
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1

if __name__ == '__main__':
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))
