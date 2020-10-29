class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        str_len = s.split(" ")
        str_len = [ ele[::-1] for ele in str_len ]

        return " ".join(str_len)

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))