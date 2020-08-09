class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = ""
        for i in range(len(s)):
            if s[i] == ' ':
                ss += "%20"
            else:
                ss += s[i]

        return ss


if __name__ == '__main__':
    s = "We are happy."
    print( Solution().replaceSpace(s) )