class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        data = [ ele for ele in s.split(" ") if ele != " " and ele != '']
        data = data[::-1]
        return " ".join(data)


if __name__ == '__main__':
    s = "the sky is blue"
    s = "  hello world!  "
    s = "a good   example"
    print( Solution().reverseWords(s) )