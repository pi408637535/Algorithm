class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        res = 0
        for ele in astr:
            temp = ord(ele) - ord('a')
            if 1 << temp & res != 0: return False
            else: res = 1 << temp | res
        return True

if __name__ == '__main__':
    s = "leetcode"
    print(Solution().isUnique(s))